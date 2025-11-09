# 🩺 General Health Chatbot (Mistral-7B via Hugging Face API + Streamlit)

An intelligent, safe, and conversational **AI Health Assistant** built with **Mistral-7B-Instruct** model and **Streamlit**.  
It provides reliable **general health information**, including causes, symptoms, precautions, recommended medicines, and related alternatives — in a friendly, WhatsApp-like chat interface.

---

## 🚀 Features

✅ Built using **Mistral-7B-Instruct** via **Hugging Face API**  
✅ Modern, WhatsApp-style **Streamlit Chat UI**  
✅ Intelligent **Prompt Engineering** for structured health responses  
✅ **Safety filters** to avoid unsafe medical guidance  
✅ Context-aware chat with memory (session-based)  
✅ Well-formatted responses with medical section headings  

---

## 🧠 Model & Prompt Design

The chatbot uses **Mistral-7B-Instruct-v0.2**, a powerful open-weight instruction-tuned model hosted on Hugging Face.

### 🩺 Prompt Logic

The assistant’s system prompt enforces structure and safety:

#### 🧩 Disease Queries
When a user asks about a **disease**, include:
- **Causes**
- **Symptoms**
- **Precautions**
- **Recommended Medicines**
- **Note:** Consult a doctor for accurate diagnosis or treatment.

#### 💊 Medicine Queries
When a user asks about a **medicine**, include:
- **Formula**
- **Uses**
- **Related Medicines**
- **Note:** Consult a doctor before use.

#### 🌿 General Wellness Queries
Provide short, friendly, science-based advice (diet, exercise, hydration, sleep, etc.)

#### ⚠️ Safety Rules
- No prescriptions, dosage, or medical instructions.  
- No content about overdose, suicide, or self-harm.  
- Always encourage consulting a licensed professional.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend / API** | Hugging Face `InferenceClient` |
| **Model** | Mistral-7B-Instruct-v0.2 |
| **Language** | Python |
| **Environment** | Virtualenv / Conda |

---

## 🧾 Requirements

Create a `requirements.txt` file with:

```bash
streamlit
huggingface_hub
transformers
accelerate
```

---

## ⚙️ Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/health-chatbot.git
   cd health-chatbot
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # (Windows)
   source .venv/bin/activate   # (Mac/Linux)
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Hugging Face Token:**
   Open `Health_chatbot.py` and replace:
   ```python
   HF_TOKEN = "your_huggingface_token_here"
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run Health_chatbot.py
   ```

6. The chatbot will open in your browser at:
   ```
   http://localhost:8501
   ```

---

## 💬 Example Interaction

**User:** What causes a sore throat?  
**Assistant:**

**Causes:** Viral or bacterial infections, allergies, or dry air.  
**Symptoms:** Pain while swallowing, hoarseness, swollen glands.  
**Precautions:** Stay hydrated, avoid cold foods, use warm saltwater gargles.  
**Recommended Medicines:** Paracetamol, lozenges (e.g., Strepsils).  
**Note:** See a doctor if the sore throat lasts more than a week.

---

## 🧑‍⚕️ Safety Disclaimer

> ⚠️ This chatbot provides **general health information only**.  
> It is **not a substitute for professional medical advice, diagnosis, or treatment**.  
> Always consult a licensed healthcare provider for any medical concerns.

---

## 🧩 Future Enhancements
- 🗣️ Add voice input/output using Whisper & TTS  
- 📱 Deploy on Hugging Face Spaces  
- 💾 Enable persistent chat memory (ChromaDB / SQLite)  
- 🌐 Add multilingual support  
- 🤖 Fine-tune on health datasets for improved accuracy  

---

## 🪪 Author
**Muhammad Huzaifa Ghani**  
Machine Learning & AI Engineer  
📍 Arfa Karim Technology Incubator, Peshawar  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/)

---

## 🩷 Acknowledgements
- [Mistral AI](https://mistral.ai/)
- [Hugging Face](https://huggingface.co/)
- [Streamlit](https://streamlit.io/)

---
