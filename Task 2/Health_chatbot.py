# from huggingface_hub import InferenceClient

# token = "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"
# client = InferenceClient(token=token)

# model_id = "mistralai/Mistral-7B-Instruct-v0.2"

# system_prompt = (
#     "You are a friendly and knowledgeable virtual medical assistant.\n"
#     "Answer general health questions clearly, safely, and briefly.\n"
#     "Do not give prescriptions or dosage instructions.\n"
#     "If expert care is needed, suggest consulting a healthcare professional."
# )

# def is_safe_input(user_input):
#     unsafe_keywords = [
#         "suicide", "overdose", "self‑harm", "kill", "die",
#         "depression", "drug dosage", "prescription", "medicine dose",
#         "anxiety attack", "diagnose", "dose"
#     ]
#     return not any(word in user_input.lower() for word in unsafe_keywords)

# print("\n🤖 General Health Chatbot (Mistral‑7B via Hugging Face API)")
# print("Type 'exit' to quit.\n")

# conversation = [{"role": "system", "content": system_prompt}]

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Chatbot: Take care and stay healthy! 💬")
#         break

#     if not is_safe_input(user_input):
#         print("Chatbot: I'm really sorry, but I can’t provide guidance on that topic. Please consult a healthcare professional for help.\n")
#         continue

#     conversation.append({"role": "user", "content": user_input})

#     # 🔧 Use chat completions API
#     response = client.chat.completions.create(
#         model=model_id,
#         messages=conversation,
#         max_tokens=200,
#         temperature=0.7
#     )

#     reply = response.choices[0].message.content.strip()
#     conversation.append({"role": "assistant", "content": reply})

#     print(f"Chatbot: {reply}\n")

from huggingface_hub import InferenceClient

# -----------------------------
# Hugging Face Token & Model
# -----------------------------
token = "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"  # your Hugging Face token
client = InferenceClient(token=token)
model_id = "mistralai/Mistral-7B-Instruct-v0.2"

# -----------------------------
# Prompt Engineering
# -----------------------------
system_prompt = """
You are a friendly and knowledgeable AI health assistant.
Your goal is to answer general health and medical-related queries clearly, safely, and empathetically.

Follow these rules:
1. **If the user asks about a disease or illness:**
   - Causes: Describe common causes.
   - Symptoms: Mention 3–5 symptoms.
   - Precautions: Suggest safe preventive measures.
   - Recommended Medicines: Mention common, over-the-counter or general medicines (no dosages).
   - Add: "Consult a qualified doctor for accurate diagnosis or dosage."

2. **If the user asks about a medicine (drug name, tablet, syrup, etc.):**
   - Formula / Active Compound: Provide the main chemical formula or key ingredient.
   - Uses: Explain what it treats or relieves.
   - Related Medicines: Suggest 2–3 similar or alternative medicines (common OTC or general ones).
   - Add: "Consult a doctor for dosage, side effects, or allergies."

3. **If the query is general health or wellness:**
   - Give a short, educational, and friendly response.

Safety First:
- Never give dosage or prescription instructions.
- If a question involves harmful intent (suicide, overdose, etc.), refuse politely and suggest medical help.
- Always keep the tone empathetic, short, and factual.
"""

# -----------------------------
# Safety Filter
# -----------------------------
def is_safe_input(user_input):
    unsafe_keywords = [
        "suicide", "overdose", "self-harm", "kill", "die",
        "depression", "drug dosage", "prescription", "medicine dose",
        "diagnose", "dose", "poison", "lethal"
    ]
    return not any(word in user_input.lower() for word in unsafe_keywords)

# -----------------------------
# Chatbot Logic
# -----------------------------
print("\n🤖 General Health Chatbot (Mistral-7B via Hugging Face API)")
print("Type 'exit' to quit.\n")

conversation = [{"role": "system", "content": system_prompt}]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Take care and stay healthy! 💬")
        break

    if not is_safe_input(user_input):
        print("Chatbot: I'm really sorry, but I can’t provide guidance on that topic. Please consult a healthcare professional for help.\n")
        continue

    conversation.append({"role": "user", "content": user_input})

    # 🔧 Generate response using chat completion API
    response = client.chat.completions.create(
        model=model_id,
        messages=conversation,
        max_tokens=350,
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()
    conversation.append({"role": "assistant", "content": reply})

    print(f"Chatbot: {reply}\n")
