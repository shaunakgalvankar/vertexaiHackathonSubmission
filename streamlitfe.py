import streamlit as st
import google.auth
import os
import json
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcpcred.json"
os.environ['GOOGLE_CLOUD_PROJECT'] = 'spyrai'

def videoMapper(name):
    videoMap = {
        "Python OOP Tutorial 1: Classes and Instances":"Tutorial_1",
        "Python OOP Tutorial 2: Class Variables": "Tutorial_2",
        "Python OOP Tutorial 3: Classmethods and Staticmethods": "Tutorial_3",
        "Python OOP Tutorial 4: Inheritance - Creating Subclasses": "Tutorial_4",
        "Python OOP Tutorial 5: Special (Magic/Dunder) Methods": "Tutorial_5",
        "Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters": "Tutorial_6",
        }
    print(videoMap[name])
    return videoMap[name]

def fetchVideoStreamignEndpoint(videoName):
    endpoint = "./videos/" + videoName + ".mp4"
    return endpoint

def fetchVideoSummary(videoName):
    with open("summarization.json", "r") as file:
        endpoint = json.load(file)
    return endpoint[videoName]

def fetchVideoTranscript(videoName):
    with open("transcripts.json", "r") as file:
        endpoint = json.load(file)
    return endpoint[videoName]

def getResponse(query, videoname):
    vertexai.init(project="spyrai", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": 0.8,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40
    }

    prompt = "Here is video transcript, I will ask question pertaining to it. Please ,make sure to answer only from transcript data and not general"
    transcrpit = fetchVideoTranscript(videoname)

    chat = chat_model.start_chat(
    
    context=prompt + transcrpit
    )
    response = chat.send_message(query, **parameters)
    print(f"{response.text}")
    with st.chat_message("🤖"):
        st.write("\n" + response.text)


st.title("SpyrAI")

with st.sidebar:
    st.write("# Videos by Corey Schafer")
    st.divider()
    radio_input = st.radio("Video list", ["Python OOP Tutorial 1: Classes and Instances","Python OOP Tutorial 2: Class Variables","Python OOP Tutorial 3: Classmethods and Staticmethods","Python OOP Tutorial 4: Inheritance - Creating Subclasses","Python OOP Tutorial 5: Special (Magic/Dunder) Methods","Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters"],)


videoPlaceholder = st.empty()
query = st.chat_input("Query?")
responsePlaceholder = st.empty()
summaryPlaceholder = st.empty()

selectedVideo = videoMapper(radio_input)
videoEndpoint = fetchVideoStreamignEndpoint(selectedVideo)

with videoPlaceholder.container():
    st.video(videoEndpoint)

with summaryPlaceholder.container():
    st.subheader("Summary")
    st.write(fetchVideoSummary(selectedVideo))

if query:
    getResponse(query,selectedVideo)
