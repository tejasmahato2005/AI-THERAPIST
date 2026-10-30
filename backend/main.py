import os
import sys

# Ensure backend directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import requests
from fastapi import FastAPI, Form, Query as FastAPIQuery, Request, Response
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import uvicorn

from ai_agent import graph, SYSTEM_PROMPT, parse_response
from config import WHATSAPP_TOKEN, WHATSAPP_PHONE_NUMBER_ID, WHATSAPP_VERIFY_TOKEN

app = FastAPI()

# Step2: Receive and validate request from Frontend (Streamlit)
class ChatMessage(BaseModel):
    message: str


@app.post("/ask")
async def ask(query: ChatMessage):
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
    stream = graph.stream(inputs, stream_mode="updates")
    tool_called_name, final_response = parse_response(stream)

    # Step3: Send response to the frontend
    return {"response": final_response,
            "tool_called": tool_called_name}


# --- Meta WhatsApp Cloud API Webhook ---

# 1. Webhook Verification (GET /webhook and GET /)
@app.get("/webhook")
@app.get("/")
async def verify_webhook(
    hub_mode: str = FastAPIQuery(None, alias="hub.mode"),
    hub_verify_token: str = FastAPIQuery(None, alias="hub.verify_token"),
    hub_challenge: str = FastAPIQuery(None, alias="hub.challenge")
):
    """
    Meta sends a GET request to verify this webhook when configuring in Meta Developer portal.
    """
    if hub_mode == "subscribe" and str(hub_verify_token) == str(WHATSAPP_VERIFY_TOKEN):
        return Response(content=hub_challenge, media_type="text/plain")
    return Response(content="Verification failed", status_code=403)


def send_whatsapp_reply(to_number: str, message_text: str):
    """Sends a WhatsApp text message back to the user via Meta Graph API."""
    url = f"https://graph.facebook.com/v21.0/{WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {"body": message_text}
    }
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=15)
        res.raise_for_status()
        print(f"WhatsApp reply sent successfully to {to_number}")
    except Exception as e:
        print(f"Error sending WhatsApp message to {to_number}: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Meta error details: {e.response.text}")



# 2. Inbound Message Handler (POST /webhook and POST /)
@app.post("/webhook")
@app.post("/")
async def receive_whatsapp(request: Request):
    """
    Receives incoming WhatsApp messages from Meta, passes them to Dr. Emily (MedGemma + AI Agent),
    and sends the therapeutic response back via WhatsApp.
    """
    data = await request.json()

    try:
        entries = data.get("entry", [])
        for entry in entries:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])

                if not messages:
                    # Could be status updates (sent, delivered, read)
                    continue

                for msg in messages:
                    sender = msg.get("from")  # user's WhatsApp number
                    msg_type = msg.get("type")

                    if msg_type == "text":
                        user_text = msg.get("text", {}).get("body", "").strip()
                    else:
                        user_text = "User sent a non-text message."

                    if not user_text:
                        continue

                    # Invoke AI Agent
                    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_text)]}
                    stream = graph.stream(inputs, stream_mode="updates")
                    tool_called_name, final_response = parse_response(stream)

                    if not final_response:
                        final_response = "I'm here to support you, but I couldn't generate a response just now. Please tell me more about how you're feeling."

                    # Send reply back to WhatsApp user
                    send_whatsapp_reply(sender, final_response)

    except Exception as e:
        import traceback
        print(f"Webhook processing error: {e}")
        traceback.print_exc()

    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir=os.path.dirname(os.path.abspath(__file__)))








