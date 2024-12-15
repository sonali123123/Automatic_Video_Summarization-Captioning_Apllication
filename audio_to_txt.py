
import os
from yt_dlp import YoutubeDL
import whisper
from pydub import AudioSegment

def download_audio(video_url: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, 'audio.%(ext)s'),
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(video_url, download=True)
    
    # Get the downloaded file path (assuming the audio is downloaded as a webm or m4a file)
    downloaded_audio_path = os.path.join(output_folder, "audio.webm")  # adjust the extension based on the downloaded format
    
    # Convert the audio to mp3 using pydub
    audio = AudioSegment.from_file(downloaded_audio_path)
    mp3_path = os.path.join(output_folder, "audio.mp3")
    audio.export(mp3_path, format="mp3")
    
    # Clean up the original downloaded file (optional)
    os.remove(downloaded_audio_path)
    
    return mp3_path

def transcribe_audio(audio_path: str, output_folder: str):
    whisper_model = whisper.load_model("base")
    try:
        result = whisper_model.transcribe(audio_path, language="english")
        transcription_text = result.get("text", "")
        os.makedirs(output_folder, exist_ok=True)
        transcription_filename = "audio_transcription.txt"
        transcription_path = os.path.join(output_folder, transcription_filename)
        with open(transcription_path, "w", encoding="utf-8") as f:
            f.write(transcription_text)
        return transcription_path
    except Exception as e:
        raise Exception(f"Failed to transcribe audio: {e}")
