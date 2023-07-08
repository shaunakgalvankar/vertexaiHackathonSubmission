import streamlit as st


st.title('SpyrAI')

video_file = open('../demo.mov', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
# Object notation
sidebar = st.sidebar.selectbox(
    "Videos",
    (video_file)
)
prompt = st.text_input("Got Questions?")


