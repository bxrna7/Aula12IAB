import streamlit as st
import speech_recognition as sr


st.title("Transcrição")
upload = st.file_uploader("Faça upload" , type=["wav"])
if upload is not None:
    recognizer = sr.Recognizer()
    with sr.AudioFile(upload) as source:
        st.write("Processando audio")
        audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio,language="pt-BR")
        st.write("Texto:" , texto)

