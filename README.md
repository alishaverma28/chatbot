# 🤖 **GenAI Chatbot (Gemini)**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-orange)](https://streamlit.io/)  
[![Gemini AI](https://img.shields.io/badge/Google_Gemini-AI-red)](https://developers.generativeai.google/)

A **web-based chatbot** powered by **Google Gemini AI**, built using **Streamlit**.  
Interact with an AI assistant in real-time with a session-based conversation history.  

---

## 🛠️ **Features**

- **Interactive chat interface** for user-AI conversations  
- **Maintains conversation history** during the session  
- Uses **Google Gemini 2.5 Flash Lite** model for AI responses  
- **Easy configuration** using a `.env` file for API keys  

---

## 💻 **Tech Stack**

- **Python**  
- **Streamlit** – Web app interface  
- **Google Generative AI (Gemini)** – AI language model  
- **python-dotenv** – Manage environment variables  

---

## ⚡ **Setup & Installation**

1. **Clone the repository**  

```bash
git clone <your-repo-url>
cd <repo-folder>
Create and activate a virtual environment

bash
Copy code
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Setup environment variables

Create a .env file in the root directory:

bash
Copy code
GOOGLE_GEMINI_API=your_api_key_here
Important: Replace your_api_key_here with your Google Gemini API key.

Run the app

bash
Copy code
streamlit run app.py
📝 Usage
Open the app in your browser (Streamlit provides the URL).

Type your questions or prompts in the chat input.

The AI responds in real-time using Google Gemini.

All messages are displayed in the chat history for the current session.

🖼️ Screenshot / Demo
Add a screenshot or GIF of your chatbot here to make your repo visually appealing.

Example Markdown:

markdown
Copy code
![Chatbot Demo](assets/chatbot_demo.gif)
💡 Notes
Keep your Gemini API key secure.

Session messages are temporary and exist only while the browser session is active.

📌 License
MIT License
