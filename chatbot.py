"""
🧠 DocuMind — Intelligent Document Q&A Assistant
A versatile chatbot that answers questions from PDFs or websites using Groq + Llama3.
Supports continuous conversation with context memory.

Author: Suryalaxmi Ravianandan
GitHub: github.com/suravi73/Insightbot
"""

import os
from dotenv import load_dotenv
from groq import Groq
import PyPDF2
import requests
from bs4 import BeautifulSoup

# Load environment variables from .env file
load_dotenv()

# Get credentials from env
api_key = os.getenv("api_key_groq")  # ✅ Use uppercase, underscores
model_name = os.getenv("model_groq", "llama3-70b-8192")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in environment variables!")

# Initialize Groq client
client = Groq(api_key=api_key)

# Extract text from a Website URL
def extract_text_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        print(f"⚠️ Error fetching URL: {e}")
        return ""

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"⚠️ Error reading PDF: {e}")
        return ""
    return text

# 🔀 Choose source: PDF or Website
print("📚 Welcome to DocuMind! Load your knowledge source.")
source_type = input("Choose source: (1) PDF  (2) Website: ").strip()

document_text = ""

if source_type == "1":
    pdf_path = input("Enter PDF path: ").strip()
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File '{pdf_path}' not found.")
        exit(1)
    document_text = extract_text_from_pdf(pdf_path)
elif source_type == "2":
    url = input("Enter URL: ").strip()
    document_text = extract_text_from_url(url)
else:
    print("❌ Invalid choice. Please run again and select 1 or 2.")
    exit(1)

if not document_text.strip():
    print("❌ Could not extract text from the selected source.")
    exit(1)

# Truncate if too long
max_chars = 28000
if len(document_text) > max_chars:
    print(f"⚠️ Truncating content from {len(document_text)} to {max_chars} chars")
    document_text = document_text[:max_chars] + "\n\n[...content truncated...]"

# Build system prompt
system_prompt = f"""You are a helpful assistant for the provided document/website content.

CONTEXT:
{document_text}

INSTRUCTIONS:
- Answer questions using ONLY the context above.
- If the answer isn't in the context, say: "I don't know based on the provided content."
- Be concise, accurate, and friendly.
- If asked about something unrelated, politely redirect to the topic.
"""

# ✅ Initialize conversation history with system prompt
conversation_history = [
    {"role": "system", "content": system_prompt}
]

print("\n🤖 DocuMind Ready! Ask anything about your content.")
print("💡 Type 'quit', 'exit', or 'bye' to end the chat.\n")

# 🔄 Main Chat Loop
while True:
    user_input = input("❓ You: ").strip()
    
    # Check for exit commands
    if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
        print(f"🤖 Thank you for using {os.getenv('PROJECT_NAME')}! Goodbye! 👋\n")
        break
    
    if not user_input:
        print("⚠️ Please enter a question.\n")
        continue
    
    # Add user message to history
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        # Call Groq API with full conversation history
        response = client.chat.completions.create(
            model=model_name,
            messages=conversation_history,
            temperature=0.2,
            max_tokens=1024
        )
        
        bot_reply = response.choices[0].message.content
        print(f"🤖 Bot: {bot_reply}\n")
        
        # Add bot reply to history (for context in next turn)
        conversation_history.append({"role": "assistant", "content": bot_reply})
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Tip: Try shortening your question or restarting the chat.\n")
        # Remove the last user message if API failed, so history stays clean
        if conversation_history and conversation_history[-1]["role"] == "user":
            conversation_history.pop()