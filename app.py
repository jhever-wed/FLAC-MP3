
import streamlit as st
from pydub import AudioSegment
import io

st.set_page_config(page_title="FLAC to MP3 Converter", layout="centered")

st.title("FLAC to MP3 Converter")

uploaded_file = st.file_uploader("Upload a FLAC file", type=["flac"])

if uploaded_file:
    try:
        audio = AudioSegment.from_file(uploaded_file, format="flac")
        mp3_io = io.BytesIO()
        audio.export(mp3_io, format="mp3")
        mp3_io.seek(0)
        st.success("Conversion complete!")
        st.download_button("Download MP3", mp3_io, file_name="converted.mp3", mime="audio/mpeg")
    except Exception as e:
        st.error(f"Error during conversion: {e}")
else:
    st.info("Please upload a FLAC file to convert it to MP3.")
