import streamlit as st

import google.auth
import os
import json
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair




# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcpcred.json"
# os.environ['GOOGLE_CLOUD_PROJECT'] = 'spyrai'

def videoMapper(name):
    videoMap = {
        "Python OOP Tutorial 1: Classes and Instances":"Tutorial_1",
        "Python OOP Tutorial 2: Class Variables": "Tutorial_2",
        "Python OOP Tutorial 3: Classmethods and Staticmethods": "Tutorial_3",
        "Python OOP Tutorial 4: Inheritance - Creating Subclasses": "Tutorial_4",
        "Python OOP Tutorial 5: Special (Magic/Dunder) Methods": "Tutorial_5",
        "PPython OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters": "Tutorial_6",
        }
    
    return videoMap[name]

def fetchVideoStreamignEndpoint(videoName):
    with open("streamingendpoints.json", "r") as file:
        endpoint = json.load(file)
        print(endpoint[videoName])
    return endpoint[videoName]

def fetchVideoSummary(videoName):
    with open("summarization.json", "r") as file:
        endpoint = json.load(file)
    return endpoint[videoName]


st.title("Vertex AI Hackathon")

with st.sidebar:
    st.write("# Videos by Corey Schafer")
    st.divider()
    radio_input = st.radio("Video list", ["Python OOP Tutorial 1: Classes and Instances","Python OOP Tutorial 2: Class Variables","Python OOP Tutorial 3: Classmethods and Staticmethods","Python OOP Tutorial 4: Inheritance - Creating Subclasses","Python OOP Tutorial 5: Special (Magic/Dunder) Methods","Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters"],)

c1, c2 = st.columns([0.8,0.2], gap="medium")


with c1.container():
    videoPlaceholder = st.empty()
    st.text_input("Chat with me")

with c2:
    summaryPlaceholder = st.empty()

q = videoMapper(radio_input)
print(videoMapper(radio_input))
v = fetchVideoStreamignEndpoint(q)

with videoPlaceholder.container():
    st.video(v)

with summaryPlaceholder.container():
    st.write(fetchVideoSummary(q))
