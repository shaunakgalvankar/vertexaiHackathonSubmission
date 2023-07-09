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

GOOGLE_APPLICATION_CREDENTIALS="./spyrai-10c4dddb2fc8.json"

with open ("credentials.json") as file:
    service_accountInfo=json.load(file)

myCredentials=service_account.Credentials.from_service_account_info(service_accountInfo)

aiplatform.init(credentials=myCredentials)

# with open ("credentials.json",encoding ="utf-8") as file:
#     project_json=json.load(file)
#     project_id=project_json("project_id")

project_id="spyrai"

vertexai.init(project=project_id,location="us-central1")

def handle_chat():
    """
    Endpoint to handle chat.
    Receives a message from the user, processes it, and returns a response from the model.
    """
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": 0.8,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40,
    }
    chat = chat_model.start_chat(  # Initialize the chat with model
        # chat context and examples go here
        context="My name is miles .You're an astronomer knowlegable about the solar system",
        examples=[
            InputOutputTextPair(
        input_text="How many moons does mars have?",
        output_text="the planet mars has 2 moons phoebus and rushang"
            )
        ]
    )
    # Send the human message to the model and get a response
    response = chat.send_message("how many planets are there inthe solar system", **parameters)
    # Return the model's response
    print(response.text)
    return {"response": response.text}

handle_chat()


# st.title('SpyrAI')
# video_url="https://www.youtube.com/watch?v=jRAAaDll34Q&ab_channel=CoreySchafer"

# st.video(video_url, start_time=0)


# sidebar = st.sidebar.selectbox(
#     "Videos",
#     ("shaunak","rushang")
# )

# prompt = st.text_input("Got Questions?")
# loader = YoutubeLoader.from_youtube_url(
#     video_url, add_video_info=True
# )

# docs=loader.load()
# transcribedText=docs[0].page_content



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

