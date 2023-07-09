import streamlit as st
import os
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain
from langchain.document_loaders import YoutubeLoader

from google.cloud import aiplatform
from langchain.text_splitter import RecursiveCharacterTextSplitter
from google.cloud import aiplatform

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='spyrai',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://my_staging_bucket',

    # custom google.auth.credentials.Credentials
    # environment default creds used if not set
    credentials="AIzaSyAf9YstQtzv5TC0VpoJ5-_2hOoq-En2vxM",

    # customer managed encryption key resource name
    # will be applied to all Vertex AI resources if set
    # encryption_spec_key_name=my_encryption_key_name,

    # the name of the experiment to use to track
    # logged metrics and parameters
    experiment='my-experiment',

    # description of the experiment above
    experiment_description='my experiment decsription'
)

st.title('SpyrAI')
<<<<<<< HEAD
# video_url="https://vertexai-usw31.streaming.media.azure.net/05f56565-77b3-4cd9-8c11-4f6c503093a2/Py_OOP_Tutorial_1_ Classes_and_I.ism/manifest(format=m3u8-cmaf)"
=======
video_url="https://www.youtube.com/watch?v=jRAAaDll34Q&ab_channel=CoreySchafer"
>>>>>>> ef89408 (google cloud init)

# st.video(video_url)


with st.sidebar:
    add_radio = st.radio("Videos",("Tutotial 1","Tutotial 2","Tutotial 3","Tutotial 4","Tutotial 5","Tutotial 6"))


st.video("https://vertexai-usw31.streaming.media.azure.net/e7a442b3-cb4f-4d5c-bb7f-e45416682956/Tutorial_6.ism/manifest(format=m3u8-cmaf)")

prompt = st.text_input("Got Questions?")
# loader = YoutubeLoader.from_youtube_url(
#     video_url, add_video_info=True
# )

<<<<<<< HEAD
# docs=loader.load()
# transcribedText=docs[0].page_content
# print(transcribedText)
=======
docs=loader.load()
transcribedText=docs[0].page_content
>>>>>>> ef89408 (google cloud init)

API_KEY=AIzaSyAf9YstQtzv5TC0VpoJ5-_2hOoq-En2vxM

#split a transcript
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
splits = text_splitter.split_text(transcribedText)

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = VertexAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)

