# 🤖 GenAI Chatbot (Gemini)

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-orange)](https://streamlit.io/)  
[![Gemini AI](https://img.shields.io/badge/Google_Gemini-AI-red)](https://developers.generativeai.google/)

A **web-based chatbot** powered by **Google Gemini AI**, built using **Streamlit**.  
Chat with an AI assistant in real-time and maintain a session-based conversation history.

---

## 🛠️ Features

- **Interactive chat interface** for user-AI conversations  
- **Maintains conversation history** during the session  
- Uses **Google Gemini 2.5 Flash Lite** model for AI responses  
- **Easy environment setup** using `.env` file for API keys  

---

## 💻 Tech Stack

- **Python**  
- **Streamlit** – Web app interface  
- **Google Generative AI (Gemini)** – AI language model  
- **python-dotenv** – Manage environment variables  

---

## ⚡ Setup & Installation

1. **Clone the repository**  

```bash
git clone <your-repo-url>
cd <repo-folder>


---
2. Create and activate a virtual environment

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

3.Install dependencies

pip install -r requirements.txt

4. Add your API key

Create a .env file in the root folder:

GOOGLE_GEMINI_API=your_api_key_here

5.Run the app

streamlit run app.py

---

📝 Usage

Open the app in your browser (Streamlit will provide the URL).

Type your questions in the chat input box.

The AI responds in real-time using Google Gemini.

All messages are displayed in order in the chat history.

---

💡 Notes

Keep your Gemini API key secure.

Session messages exist only while the browser session is active.


