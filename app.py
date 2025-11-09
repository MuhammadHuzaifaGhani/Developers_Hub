# ==============================================
# 🩺 General Health Chatbot (Mistral-7B Streamlit App)
# ==============================================
import streamlit as st
from huggingface_hub import InferenceClient
import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="🩺 Health Assistant Chatbot",
    page_icon="💬",
    layout="centered"
)

# -----------------------------
# HUGGING FACE MODEL CONFIG
# -----------------------------
HF_TOKEN = "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"  # Replace with your token
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

client = InferenceClient(token=HF_TOKEN)

# -----------------------------
# PROMPT ENGINEERING
# -----------------------------

SYSTEM_PROMPT = """
You are a friendly and knowledgeable AI medical assistant.
Your goal is to provide clear, safe, and empathetic health information in a structured format.

Your responses must always follow this exact format using bold markdown headings:

If the query is about a **disease or illness**, respond using:
**🩸 Causes:**  
- Briefly explain the main reasons behind the condition.  
**🤒 Symptoms:**  
- List 3–5 key symptoms.  
**🧘‍♀️ Precautions:**  
- Give simple prevention or care advice.  
**💊 Recommended Medicines:**  
- Mention common or over-the-counter options (do not include dosage).  
**⚠️ Note:**  
- Always remind the user to consult a healthcare professional for diagnosis and treatment.

If the query is about a **medicine**, respond using:
**🧪 Formula:**  
- Write the main active compound or chemical formula.  
**💡 Uses:**  
- Explain what the medicine is used for.  
**💊 Related Medicines:**  
- Suggest 2–3 similar or alternative medicines.  
**⚠️ Note:**  
- Remind the user to consult a doctor for dosage, allergies, or side effects.

If the question is about **general health or wellness** (e.g., diet, sleep, hydration):
- Provide a short, positive, and informative answer in friendly language.
- Use bullet points if needed.

**General Guidelines:**
- Keep responses concise (under 200 words).  
- Use markdown formatting (**bold**, lists, emojis for sections).  
- Never give prescription doses or medical instructions.  
- Avoid mental health crisis topics (suicide, overdose, self-harm).  
- Maintain a warm, trustworthy, and professional tone.
"""

# -----------------------------
# SAFETY FILTER
# -----------------------------
def is_safe_input(user_input):
    unsafe_keywords = [
        "suicide", "overdose", "self-harm", "kill", "die",
        "depression", "drug dosage", "prescription", "medicine dose",
        "diagnose", "dose", "poison", "lethal"
    ]
    return not any(word in user_input.lower() for word in unsafe_keywords)

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "👋 Hello! I'm your friendly Health Assistant. How can I help you today?"}]

# -----------------------------
# APP UI
# -----------------------------
st.markdown("""
    <style>
        .chat-container {
            max-height: 70vh;
            overflow-y: auto;
            padding: 10px;
            border-radius: 10px;
            background-color: #e5ddd5;
        }
        .user-message {
            background-color: #dcf8c6;
            padding: 10px;
            border-radius: 10px;
            margin: 8px 0;
            text-align: right;
        }
        .bot-message {
            background-color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 8px 0;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🩺 Health Assistant Chatbot")

# -----------------------------
# DISPLAY CHAT MESSAGES
# -----------------------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-message'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-message'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.chat_input("Type your health question here...")

if user_input:
    if not is_safe_input(user_input):
        st.session_state.messages.append({"role": "assistant", "content": "⚠️ Sorry, I can’t provide guidance on that topic. Please consult a healthcare professional."})
        st.rerun()

    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Prepare chat history for model
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages

    with st.spinner("💭 Thinking..."):
        try:
            response = client.chat.completions.create(
                model=MODEL_ID,
                messages=conversation,
                max_tokens=350,
                temperature=0.7
            )
            bot_reply = response.choices[0].message.content.strip()
        except Exception as e:
            bot_reply = f"⚠️ Oops! There was an error: {e}"

    # Add bot reply to session
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.rerun()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("<br><center>💚 Built with Streamlit & Mistral-7B | Safe General Health Info Only</center>", unsafe_allow_html=True)
