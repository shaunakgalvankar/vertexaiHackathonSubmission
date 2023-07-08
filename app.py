import streamlit as st
import os
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain
from langchain.document_loaders import YoutubeLoader

st.title('SpyrAI')
video_url="https://www.youtube.com/watch?v=Azyizl9w2xo"

st.video(video_url, start_time=0)


sidebar = st.sidebar.selectbox(
    "Videos",
    ("shaunak","rushang")
)

prompt = st.text_input("Got Questions?")
loader = YoutubeLoader.from_youtube_url(
    video_url, add_video_info=True
)

docs=loader.load()
transcribedText=docs[0].page_content
print(transcribedText)




