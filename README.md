<div align="center">

### Autonomous AI Mental Health Therapist & Real-Time Crisis Intervention Agent

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-f55036?style=for-the-badge&logo=fastlane&logoColor=white)](https://groq.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Workflow-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![Meta WhatsApp](https://img.shields.io/badge/WhatsApp-Cloud%20API%20v21.0-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://developers.facebook.com/)
[![Google Maps](https://img.shields.io/badge/Google%20Maps-Places%20%26%20Geocode-4285F4?style=for-the-badge&logo=googlemaps&logoColor=white)](https://developers.google.com/maps)
[![Twilio](https://img.shields.io/badge/Twilio-Voice%20Intervention-F22F46?style=for-the-badge&logo=twilio&logoColor=white)](https://www.twilio.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Interface-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Deployment](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

<p align="center">
  <b>A compassionate, 24/7 AI-driven psychological companion equipped with autonomous clinical reasoning, automated life-saving crisis voice dispatch, licensed therapist geo-discovery, and dual omnichannel availability (WhatsApp & Web).</b>
</p>

[Key Features](#-key-features) • [Why SafeSpace](#-why-safespace-works) • [System Architecture](#-system-architecture) • [Tools & Tech Stack](#-technology-stack--apis) • [Quickstart Guide](#-installation--setup) • [Deployment](#-cloud-deployment-render) • [Safety & Ethics](#-safety--ethical-guardrails)

---

</div>

## 📖 Overview

**SafeSpace 2.0** is an intelligent, multi-tool agentic mental health platform designed to bridge the accessibility gap in emotional and psychological care. Built upon modern cognitive AI architectures (**LangGraph ReAct Pattern** and **Groq LPUs**), SafeSpace does not simply regurgitate canned answers—it actively reasons about a user's emotional state, selects specialized clinical tools, and intervenes proactively when danger is sensed.

Users can converse naturally with **Dr. Emily Hartman**—a clinically attuned AI psychologist persona—either directly from **WhatsApp** (leveraging the Meta Graph Cloud API) or via an intuitive **Streamlit Web Portal**. If a user expresses severe trauma, despair, or suicidal thoughts, SafeSpace autonomously breaks conversational mode and triggers an **instant emergency phone call** to designated crisis responders via Twilio.

---

## ✨ Key Features

- 🩺 **Clinical Empathy Engine (Dr. Emily Hartman)**: Utilizes specialized therapeutic conversation modeling (emotional attunement, normalization, practical guidance, and strengths-focused questioning) without sterile medical jargon.
- ⚡ **Ultra-Low Latency Inference**: Powered by **Groq Cloud LPUs** executing the high-parameter `openai/gpt-oss-120b` reasoning model in milliseconds.
- 🛡️ **Autonomous Crisis Escalation (Twilio Voice)**: Instantly detects suicidal ideation or self-harm intentions and autonomously places an urgent voice call to emergency contacts or safety helplines.
- 📍 **Real-Time Geocoded Therapist Finder (Google Maps API)**: Analyzes user queries like *"Find someone near Kolkata"* or *"Therapist in San Francisco"*, converts locations to coordinates, and returns real verified psychotherapist clinics with phone numbers and addresses within a 5 km radius.
- 💬 **Omnichannel Integration (Meta WhatsApp Cloud API)**: Native webhook integration supporting official Meta WhatsApp Cloud API v21.0, featuring automated 4000-character intelligent message splitting for smooth chat delivery.
- 🌐 **Interactive Streamlit Web Dashboard**: Clean browser interface displaying real-time agent responses alongside visible tool-dispatch indicators (`[ask_mental_health_specialist]`, `[emergency_call_tool]`, `[find_nearby_therapists_by_location]`).
- 🔒 **Production-Hardened Sanitization**: Immune to HTTP header newline corruption bugs, whitespace-stripped environment reads, and resilient request retry mechanisms.

---

## 🎯 Why SafeSpace Works

| Traditional Chatbots | SafeSpace 2.0 Agentic Architecture |
| :--- | :--- |
| **Static Scripted Responses**: Repetitive, generic advice that feels cold and robotic. | **Attuned Persona Reasoning**: Dr. Emily Hartman applies genuine clinical psychology frameworks. |
| **Isolated Silo**: Cannot interact with external real-world services. | **Multi-Tool Autonomous Action**: Can call phones, look up map data, and search specialized models. |
| **Passive in Emergencies**: Prints a helpline number that a person in crisis may be unable to dial. | **Active Life-Saving Escalation**: Automatically dials the crisis helpline / emergency guardian in real time. |
| **Closed Ecosystem**: Trapped within custom proprietary apps. | **Frictionless WhatsApp Access**: Available on the messaging app 2+ billion people already have in their pocket. |

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Clients["Omnichannel User Frontends"]
        WA[("📱 WhatsApp User")] <-->|HTTPS Webhook| META["Meta WhatsApp Cloud API v21.0"]
        WEB["💻 Streamlit Web UI"] <-->|POST /ask| FASTAPI["⚡ FastAPI Backend Engine\n(Uvicorn / Render)"]
    end

    META <-->|POST /webhook\nGET /webhook (Challenge)| FASTAPI

    subgraph AgenticCore["LangGraph Autonomous ReAct Core"]
        FASTAPI --> AGENT["🤖 LangGraph ReAct Agent\n(Groq LPU: openai/gpt-oss-120b)"]
        AGENT --> REASON{"Clinical Intent Reasoning\n& State Assessment"}
    end

    subgraph Tools["Autonomous Tool Arsenal"]
        REASON -->|"General Emotional Support"| T1["🩺 ask_mental_health_specialist\n(Dr. Emily Persona Prompt + Groq)"]
        REASON -->|"Local Help Query"| T2["📍 find_nearby_therapists_by_location\n(Google Maps Geocoding & Places API)"]
        REASON -->|"Self-Harm / Crisis Detected"| T3["🚨 emergency_call_tool\n(Twilio Voice REST API Call)"]
    end

    T1 --> DISPATCH["Unified Response Parser"]
    T2 --> DISPATCH
    T3 --> DISPATCH

    DISPATCH -->|"WhatsApp Splitter (Max 4000 Chars)"| META
    DISPATCH -->|"JSON Payload"| WEB
```

---

## 🛠️ Technology Stack & APIs

### 1. Core Languages & Runtime
- **Python 3.11+**: Fast, modern typed Python runtime.
- **FastAPI**: High-performance asynchronous REST API framework handling inbound webhooks and frontend queries.
- **Uvicorn**: Lightning-fast ASGI web server implementation.
- **uv / pip**: Cutting-edge Python packaging and dependency management.

### 2. Large Language Models & AI Agent Orchestration
- **Groq LPU (Language Processing Unit)**: Near-zero latency inference provider.
- **`openai/gpt-oss-120b`**: Massive 120B parameter reasoning model running on Groq, delivering thoughtful clinical judgment and tool execution.
- **LangGraph & LangChain (`langgraph.prebuilt.create_react_agent`)**: ReAct (Reasoning + Acting) loop managing agent decisions, state management, and tool call routing.
- **MedGemma / Dr. Emily Framework**: Specialized therapeutic prompt template enforcing emotional attunement, normalization, practical guidance, and strengths-focused questioning.

### 3. External Cloud APIs & Services
- **Meta WhatsApp Cloud API (Graph API v21.0)**: Direct webhook integration enabling two-way WhatsApp messaging with verify-token handshakes and payload parsing.
- **Twilio Voice API**: Automated telephone dispatch service initiating outbound calls (`client.calls.create`) with programmable TwiML voice scripts during emergency triggers.
- **Google Maps Platform (Geocoding + Places API)**:
  - *Geocoding API*: Converts human location inputs (*e.g., "Kolkata", "Brooklyn"*) into exact latitude and longitude.
  - *Places API (`places_nearby` & `place`)*: Queries licensed psychotherapists within a 5000-meter radius, retrieving verified clinic names, vicinity addresses, and telephone numbers.
- **Render Cloud Platform**: Production server hosting the containerized FastAPI backend with continuous CI/CD GitHub deployment.
- **Streamlit**: Rapid web application framework rendering the conversational browser UI.

---

## 📂 Project Directory Structure

```text
ai-therapist-2.0/
├── backend/
│   ├── ai_agent.py          # LangGraph ReAct agent definition, tools binding & system prompt
│   ├── config.py            # Environment configuration with automatic whitespace sanitation (.strip())
│   ├── main.py              # FastAPI server, Meta WhatsApp webhooks (/webhook), & /ask API
│   ├── tools.py             # Tool implementations: Dr. Emily LLM generator & Twilio emergency caller
│   └── test_location_tool.py# Isolated unit test suite for Google Maps Therapist Finder
├── frontend.py              # Streamlit interactive web interface
├── pyproject.toml           # Modern project specifications & uv dependencies
├── requirements.txt         # Production pip dependency manifest
├── .gitignore               # Environment and secret exclusions
└── README.md                # Comprehensive project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python **3.11** or higher
- Git
- API Keys for:
  - [Groq Cloud](https://console.groq.com/)
  - [Google Maps Platform](https://console.cloud.google.com/) (Enable **Geocoding API** and **Places API**)
  - [Twilio Console](https://www.twilio.com/) (Account SID, Auth Token, Twilio Phone Number)
  - [Meta for Developers](https://developers.facebook.com/) (WhatsApp Cloud API App)

### 1. Clone Repository & Setup Environment

```bash
# Clone the repository
git clone https://github.com/tejasmahato2005/AI-THERAPIST.git
cd AI-THERAPIST

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# macOS / Linux:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

*(Alternatively, if using `uv`: `uv sync && source .venv/bin/activate`)*

---

### 2. Configure Environment Variables

Create a `.env` file or populate your hosting environment variables with the following keys:

| Environment Variable | Description | Example / Format |
| :--- | :--- | :--- |
| `GROQ_API_KEY` | Groq Cloud API Key for ultra-fast LPU inference | `gsk_xxxxxxxxxxxxxxxxxxxx` |
| `GOOGLE_MAPS_API_KEY` | Google Maps API key with Geocoding & Places enabled | `AIzaSyxxxxxxxxxxxxxxxxxxxx` |
| `TWILIO_ACCOUNT_SID` | Twilio Account SID for voice dispatch | `ACxxxxxxxxxxxxxxxxxxxxxxxx` |
| `TWILIO_AUTH_TOKEN` | Twilio Authentication Token | `xxxxxxxxxxxxxxxxxxxxxxxx` |
| `TWILIO_FROM_NUMBER` | Twilio purchased virtual phone number | `+1234567890` |
| `EMERGENCY_CONTACT` | Designated crisis contact phone number to receive urgent calls | `+919876543210` |
| `WHATSAPP_TOKEN` | Permanent Meta System User Access Token | `EAAxxxxxxxxxxxxxxxxxxxx` |
| `WHATSAPP_PHONE_NUMBER_ID` | WhatsApp Business Phone Number ID from Meta Portal | `1439658252553805` |
| `WHATSAPP_VERIFY_TOKEN` | Custom verification secret string for Meta Webhook setup | `200506` *(or custom)* |

> **Pro Tip:** In `backend/config.py`, all variables are systematically cleaned using `.strip()` to ensure accidental trailing newlines or whitespace (which cause `httpx.LocalProtocolError: Illegal header value`) never crash your production server.

---

### 3. Running Locally

#### Step A: Launch the FastAPI Backend
```bash
# From workspace root
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
The backend will boot on `http://localhost:8000`.

#### Step B: Launch the Streamlit Web Interface
In a separate terminal window:
```bash
streamlit run frontend.py
```
Open `http://localhost:8501` to chat with Dr. Emily through the web dashboard.

---

## 📲 Meta WhatsApp Cloud API Setup

1. **Expose your local server (if testing locally)**:
   ```bash
   ngrok http 8000
   ```
   Copy the public HTTPS forwarding URL (e.g., `https://xyz.ngrok-free.app`).

2. **Configure Webhook in Meta Developers Portal**:
   - Navigate to **WhatsApp** ➔ **Configuration**.
   - Set **Callback URL**: `https://<YOUR_DOMAIN>/webhook` (or `https://<YOUR_DOMAIN>/`).
   - Set **Verify Token**: Must match your `WHATSAPP_VERIFY_TOKEN` (default: `200506`).
   - Click **Verify and Save**.

3. **Subscribe to Webhook Fields**:
   - Under Webhook fields, click **Manage** and subscribe to **`messages`**.

4. **Send a Message**:
   - Open WhatsApp on your phone and send any message (*e.g., "Hello Dr. Emily, I've had a tough week"*) to your test number.
   - SafeSpace processes the message and responds in seconds!

---

## 🚀 Cloud Deployment (Render)

SafeSpace is optimized for 1-click cloud hosting on [Render](https://render.com):

1. **Create Web Service**: Link your GitHub repository (`AI-THERAPIST`).
2. **Environment**: `Python 3`
3. **Build Command**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Start Command**:
   ```bash
   uvicorn backend.main:app --host 0.0.0.0 --port $PORT
   ```
5. **Add Environment Variables**: Add all variables from the table above in Render's **Environment** tab.
6. **Set Webhook in Meta**: Update your Meta Developer Webhook callback URL to `https://your-render-service.onrender.com/webhook`.

---

## 📡 REST API Reference

### 1. `POST /ask`
Direct JSON endpoint for web frontends, mobile applications, or external services.

- **Request Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "message": "Can you recommend a licensed therapist in Boston?"
  }
  ```
- **Response**:
  ```json
  {
    "response": "I'd be glad to help you find local support. Here are licensed therapists located near Boston:\n- Boston Center for Therapy | 123 Commonwealth Ave | (617) 555-0199\n...",
    "tool_called": "find_nearby_therapists_by_location"
  }
  ```

---

### 2. `GET /webhook`
Meta Graph API Webhook Verification endpoint.
- Validates `hub.mode == "subscribe"` and `hub.verify_token == WHATSAPP_VERIFY_TOKEN`.
- Echoes back `hub.challenge` as plain text.

---

### 3. `POST /webhook`
Inbound WhatsApp Message Event Receiver.
- Extracts sender phone number and message payload.
- Streams user query through the LangGraph agent.
- Automatically splits responses exceeding **4000 characters** into ordered sequential messages to honor WhatsApp's 4096-character limit.

---

## 🛡️ Safety & Ethical Guardrails

> [!CAUTION]
> **Emergency Notice**: SafeSpace 2.0 is an assistive AI research project and technology demonstration. It does **not** provide clinical psychiatric diagnosis or replace certified medical personnel.

### Built-in Safety Mechanisms:
1. **Autonomous Emergency Escalation**: The agent's cognitive graph monitors every turn for red-flag intent markers (suicide, self-harm, violent despair). If triggered, the agent prioritizes the `emergency_call_tool`, placing an instantaneous voice call to emergency numbers.
2. **Non-Judgmental Clinical Framing**: Responses adhere to strict empathetic psychology standards without patronizing or providing invalidating medical claims.
3. **Local Professional Handoff**: Whenever long-term therapy is appropriate, SafeSpace leverages Google Maps to bridge users to real, certified human professionals in their locality.

---

## 🧪 Testing

Test the Google Maps therapist locator independently:
```bash
python backend/test_location_tool.py
```
Expected output:
```text
Therapists near Kolkata:
- Mind & Brain Clinic | Park Street | +91 33 2222 xxxx
- Compassionate Minds | Salt Lake | +91 98 3000 xxxx
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License & Credits

Distributed under the MIT License. See `LICENSE` for more information.

Developed with ❤️ by [Tejas Mahato](https://github.com/tejasmahato2005) & Contributors.
Special acknowledgment to **Groq**, **LangChain**, **Meta**, **Twilio**, and **Google Maps Platform** for powering accessible AI infrastructure.
