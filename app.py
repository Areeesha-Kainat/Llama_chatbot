import streamlit as st
import ollama

# Streamlit UI Setup
st.set_page_config(page_title="Llama 3.2 Chatbot", layout="centered")
st.title("💬 Llama 3.2 Chatbot")
st.caption("Powered by Ollama & Streamlit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
# prompt = st.chat_input("Ask me anything...")
prompt = st.text_input("Ask me anything...")

if prompt:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get Llama Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(model="llama3.2", messages=st.session_state.messages)
            reply = response["message"]["content"]
            st.markdown(reply)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": reply})
