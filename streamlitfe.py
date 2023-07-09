import streamlit as st

import google.auth
import os
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcpcred.json"
# os.environ['GOOGLE_CLOUD_PROJECT'] = 'spyrai'

st.title("Vertex AI Hackathon")

with st.sidebar:
    st.write("# Videos by Corey Schafer")
    st.divider()
    radio_input = st.radio(" ", ["Python OOP Tutorial 1","Python OOP Tutorial 2","Python OOP Tutorial 3","Python OOP Tutorial 4","Python OOP Tutorial 5","Python OOP Tutorial 6"],)

videoPlaceholder = st.empty()

st.text_input("Chat with me")