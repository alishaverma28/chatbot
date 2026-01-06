import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

st.set_page_config(page_title="GenAI Chatbot", page_icon="🤖")
st.title("🤖 GenAI Chatbot (Gemini)")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_box = st.empty()
        response = model.generate_content(prompt)
        response_box.markdown(response.text)

    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )
