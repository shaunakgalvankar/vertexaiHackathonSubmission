import streamlit as st
import os
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain
from langchain.document_loaders import YoutubeLoader

st.title('SpyrAI')
# video_url="https://vertexai-usw31.streaming.media.azure.net/05f56565-77b3-4cd9-8c11-4f6c503093a2/Py_OOP_Tutorial_1_ Classes_and_I.ism/manifest(format=m3u8-cmaf)"

# st.video(video_url)


with st.sidebar:
    add_radio = st.radio("Videos",("Tutotial 1","Tutotial 2","Tutotial 3","Tutotial 4","Tutotial 5","Tutotial 6"))


st.video("https://vertexai-usw31.streaming.media.azure.net/e7a442b3-cb4f-4d5c-bb7f-e45416682956/Tutorial_6.ism/manifest(format=m3u8-cmaf)")

prompt = st.text_input("Got Questions?")
# loader = YoutubeLoader.from_youtube_url(
#     video_url, add_video_info=True
# )

# docs=loader.load()
# transcribedText=docs[0].page_content
# print(transcribedText)




