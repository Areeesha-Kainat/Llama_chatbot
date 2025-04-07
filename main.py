import streamlit as st
import ollama

st.set_page_config(page_title="Llama Chatbot", layout="centered")
st.title("💬 Llama 3.2 Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # response = ollama.chat(model="llama3.2", messages=st.session_state.messages, stream=True)
            response = ollama.chat(model="mistral", messages=st.session_state.messages, stream=True)

            full_response = ""
            response_container = st.empty()  # Placeholder for streaming output
            
            for chunk in response:
                full_response += chunk['message']['content']
                response_container.markdown(full_response)  # Update UI with each chunk

    st.session_state.messages.append({"role": "assistant", "content": full_response})
