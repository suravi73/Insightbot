# 🧠 Insightbot
  [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Groq API](https://img.shields.io/badge/Groq-API-black.svg?logo=fastapi&logoColor=white)](https://console.groq.com/)
[![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0+-lightgrey.svg)](https://pypdf2.readthedocs.io/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12+-3C994C.svg?logo=python&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-2.31+-FF6B6B.svg?logo=python&logoColor=white)](https://requests.readthedocs.io/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-1.0+-000000.svg?logo=python&logoColor=white)](https://pypi.org/project/python-dotenv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



**Intelligent Q&A Assistant** — Ask questions about any PDF or website, and get accurate, context-aware answers powered by Groq + Llama3.

## ✨ Features
- **Multi-Source Support**: Load knowledge from PDF files or website URLs
- **Continuous Conversation**: Chat naturally with context memory
- **Fast & Efficient**: Powered by Groq's low-latency Llama3 inference
- **Private & Secure**: API keys managed via `.env`; no data stored externally
- **Accurate Answers**: Strict context adherence to avoid hallucinations

## 🛠 Tech Stack

| Category | Technology | Purpose |
|----------|------------|---------|
|  Language | **Python 3.9+** | Core programming |
|  LLM API | **Groq** | Fast Llama3 inference |
|  PDF Processing | **PyPDF2** | Extract text from PDFs |
|  Web Scraping | **BeautifulSoup4 + Requests** | Fetch & parse website content |
|  Configuration | **python-dotenv** | Manage API keys securely |

---

## 🚀 Quick Start

**Prerequisites**
- Python 3.9 or higher
- [Groq API Key](https://console.groq.com/keys) (free tier available)
  
```bash
1. Clone the Repository

  git clone https://github.com/suravi73/insightbot.git
  cd insightbot

2. Create & Activate Virtual Environment

  # macOS/Linux
    python3.9 -m venv venv
    source venv/bin/activate

  # Windows
    python -m venv venv
    venv\Scripts\activate

3. Install Dependencies

    pip install -r requirements.txt

4. Configure Environment Variables

  # Copy the example file
    cp .env.example .env
  # Edit .env and add your Groq API key
  # api_key_groq = gsk_your_key_here

5. Run Insightbot

  python chatbot.py

```

## 💻 Usage

**Example Session**
```bash 
📚 Welcome to Insightbot! Load your knowledge source.
Choose source: (1) PDF  (2) Website: 2
Enter URL: https://suryasbloom.com

🤖 Insightbot Ready! Ask anything about your content.
💡 Type 'quit', 'exit', or 'bye' to end the chat.

❓ You: What services does Surya's Bloom offer?
🤖 Bot: Surya's Bloom offers Bach flower remedy consultations, zodiac-based wellness guidance...

❓You: How do I book a consultation?
🤖 Bot: You can book a consultation by visiting the "Contact" page or emailing...

❓ You: quit🤖 Thank you for using Insightbot! Goodbye! 👋
```

            
## 🔐 Security Best Practices

- Never commit .env: It contains your API keys.
- Use .env.example: Provide a template for others.
- Rotate keys regularly: Update your Groq API key periodically.
- Limit token usage: Monitor your Groq dashboard for usage limits.

## ⚙️ Configuration

**Environment Variables (.env)**

- api_key_groq=gsk_your_actual_key_here
- model_groq=llama3-70b-8192

**Available Groq Models**

- llama3-70b-8192 — Most powerful, best for complex reasoning
- llama3-8b-8192 — Faster, good for simple Q&A
- mixtral-8x7b-32768 — Large context window (32k tokens)

## 🧪 Testing

**Verify Installation**
```bash
python -c "import groq, PyPDF2, requests, bs4, dotenv; print('✅ All dependencies installed!')"
```
**Test PDF Extraction**
```bash 
python -c "
import PyPDF2
reader = PyPDF2.PdfReader('test.pdf')
print(reader.pages[0].extract_text()[:200])
"
```
**Test Web Scraping**
```bash
python -c"
import requests
from bs4 import BeautifulSoup
r = requests.get('https://httpbin.org/html')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.get_text()[:200])
"
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:
```bash 
- Fork the repository
- Create a feature branch: git checkout -b feature/amazing-feature
- Commit changes: git commit -m 'Add amazing feature'
- Push to branch: git push origin feature/amazing-feature
 -Open a Pull Request
```


## 📄 License

This project is licensed under the MIT License — see the LICENSE file for details.

## 🙏 Acknowledgments

This project is built with gratitude for:

- ⚡ **[Groq](https://groq.com)** — for providing fast, affordable LLM inference that makes real-time AI accessible
- 🦙 **[Llama 3](https://ai.meta.com/llama/)** — for the powerful, open-source foundation model powering Insightbot
- 🕷️ **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** — for simplifying web scraping in Python
- 🌍 **[The Open-Source Community](https://opensource.org)** — for the incredible Python libraries that make projects like this possible

## 📬 Contact

**Suryalaxmi Ravianandan**
- 📧 suryalaxmi.ravianandan@gmail.com
- 🔗 [LinkedIn](www.linkedin.com/in/suryalaxmi-ravianandan)
- 🐙 [GitHub](https://github.com/suravi73)
- 
<p align="center">
  <em>Built with ❤️ by <a href="https://github.com/suravi73">Suryalaxmi Ravianandan</a></em>
</p>
