import streamlit as st
import google.generativeai as genai

st.title("welcome to gemini chat")
genai.configure(api_key="AIzaSyBDbPmUZAZJe9QIDCJcwF0_R3mJyUymfag")
text = st.text_input("enter your question")


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("Click me"):
    response = chat.send_message(text)

    st.write(response.text)
