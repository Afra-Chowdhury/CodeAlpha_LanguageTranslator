import streamlit as st
from googletrans import Translator
import pyperclip
from gtts import gTTS
import os

translator = Translator()

st.set_page_config(page_title="Language Translation Tool", page_icon="🌍", layout="centered")
st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages using Google Translator API.")

text = st.text_area("Enter text to translate:", height=150)

lang_dict = {
    "English": "en", "Bengali": "bn", "Hindi": "hi", "French": "fr", 
    "German": "de", "Spanish": "es", "Chinese": "zh-cn", "Japanese": "ja"
}
col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source Language", list(lang_dict.keys()), index=0)
with col2:
    dest_lang = st.selectbox("Target Language", list(lang_dict.keys()), index=1)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        translated = translator.translate(text, src=lang_dict[src_lang], dest=lang_dict[dest_lang])
        st.success(f"✅ Translated Text ({dest_lang}):")
        st.write(translated.text)

        if st.button("📋 Copy to Clipboard"):
            pyperclip.copy(translated.text)
            st.info("Text copied to clipboard!")

        tts = gTTS(translated.text, lang=lang_dict[dest_lang])
        tts.save("translated_audio.mp3")
        audio_file = open("translated_audio.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
        audio_file.close()
        os.remove("translated_audio.mp3")
