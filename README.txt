
# Audio to MP3 Converter Web App

This Streamlit app allows you to convert `.flac` or `.wav` audio files to `.mp3` format using Python and FFmpeg.

## 📦 Requirements

- Python 3.7+
- `streamlit`
- `pydub`
- `ffmpeg` (must be installed separately)

## ✅ Install FFmpeg

### On Windows:
1. Download from https://ffmpeg.org/download.html
2. Extract and add the `bin` folder to your System PATH.

### On macOS:
```bash
brew install ffmpeg
```

### On Ubuntu/Linux:
```bash
sudo apt update
sudo apt install ffmpeg
```

## 🚀 Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
```
