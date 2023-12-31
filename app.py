import streamlit as st
import os
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain
from langchain.document_loaders import YoutubeLoader
import json
from google.oauth2 import service_account
import vertexai
from vertexai.preview.language_models import ChatModel,InputOutputTextPair

from google.cloud import aiplatform
from langchain.text_splitter import RecursiveCharacterTextSplitter
from google.cloud import aiplatform





st.title('SpyrAI')
video_url="https://www.youtube.com/watch?v=jCzT9XFZ5bw&ab_channel=CoreySchafer"

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
transcripts={"Tutorial_6.mp4":transcribedText}
print(transcripts)
with open('transcripts6.json', 'w') as fp:
    json.dump(transcripts, fp)




# #split a transcript
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
# splits = text_splitter.split_text(transcribedText)

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# llm = VertexAI()


# llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

# llm_chain.run(question)

