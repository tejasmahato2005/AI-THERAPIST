from groq import Groq
from config import GROQ_API_KEY

def query_medgemma(prompt: str) -> str:
    """
    Therapeutic response using Dr. Emily Hartman personality via Groq cloud API.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
    Respond to patients with:
    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...")

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Always keep conversation going by asking open-ended questions to dive into root cause.
    """
    try:
        client = Groq(api_key=GROQ_API_KEY, max_retries=3, timeout=60.0)
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return "I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."



# Step2: Setup Twilio calling API tool
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def call_emergency() -> str:
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=EMERGENCY_CONTACT,
            from_=TWILIO_FROM_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml"  # Can customize message
        )
        msg = f"Emergency call initiated successfully to {EMERGENCY_CONTACT}. Call SID: {call.sid}"
        print(msg)
        return msg
    except Exception as e:
        err = f"Failed to place emergency call: {str(e)}"
        print(err)
        return err


# Step3: Setup Location tool


