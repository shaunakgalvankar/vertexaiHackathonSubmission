import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

import streamlit as st


def generateQuery(query):
    vertexai.init(project="", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 1024,
        "top_p": 0.8,
            "top_k": 40
    }
    chat = chat_model.start_chat(
        context=query,
    )
    response = chat.send_message(query, **parameters)
    print(f"Response from Model: {response.text}")
    return response.text


question = st.text_input("Chat with me")

if question:
    ans = generateQuery(question)
    st.write(ans)