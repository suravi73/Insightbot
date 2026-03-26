# 🧠 Insightbot
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Groq-000000?style=for-the-badge&logo=fastapi&logoColor=white" alt="Groq" />
  <img src="https://img.shields.io/badge/PyPDF2-Library-000000?style=for-the-badge" alt="PyPDF2" />
  <img src="https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-000000?style=for-the-badge" alt="BeautifulSoup" />
  <img src="https://img.shields.io/badge/Requests-HTTP-000000?style=for-the-badge" alt="Requests" />
  <img src="https://img.shields.io/badge/DotEnv-Config-000000?style=for-the-badge" alt="DotEnv" />
</p>


**Intelligent Q&A Assistant** — Ask questions about any PDF or website, and get accurate, context-aware answers powered by Groq + Llama3.

## ✨ Features
- 📄 **Multi-Source Support**: Load knowledge from PDF files or website URLs
- 💬 **Continuous Conversation**: Chat naturally with context memory
- ⚡ **Fast & Efficient**: Powered by Groq's low-latency Llama3 inference
- 🔒 **Private & Secure**: API keys managed via `.env`; no data stored externally
- 🎯 **Accurate Answers**: Strict context adherence to avoid hallucinations

## 🛠 Tech Stack
- Python 3.11+
- Groq API (LLM inference)
- PyPDF2 (PDF text extraction)
- BeautifulSoup4 + requests (web scraping)
- python-dotenv (secure config)

## 🚀 Quick Start
```bash
# 1. Clone & setup
git clone https://github.com/suravi73/Insightbot.git
cd Insightbot
python3.11 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env with your api_key_groq

# 4. Run the bot
python chatbot.py