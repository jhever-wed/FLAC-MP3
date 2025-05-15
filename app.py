
import streamlit as st
from pydub import AudioSegment
import io
import shutil

st.set_page_config(page_title="Audio to MP3 Converter", layout="centered")
st.title("FLAC/WAV to MP3 Converter")

# Check for ffmpeg
ffmpeg_path = shutil.which("ffmpeg")
if not ffmpeg_path:
    st.error("FFmpeg is not installed or not in your system PATH.\n"
             "Please install FFmpeg to enable audio conversion.")
    st.stop()

# Set converter path for pydub
AudioSegment.converter = ffmpeg_path

uploaded_file = st.file_uploader("Upload a FLAC or WAV file", type=["flac", "wav"])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    try:
        audio = AudioSegment.from_file(uploaded_file, format=file_type)
        mp3_io = io.BytesIO()
        audio.export(mp3_io, format="mp3")
        mp3_io.seek(0)
        st.success("Conversion complete!")
        st.download_button("Download MP3", mp3_io, file_name="converted.mp3", mime="audio/mpeg")
    except Exception as e:
        st.error(f"Error during conversion: {e}")
else:
    st.info("Please upload a FLAC or WAV file to convert it to MP3.")
