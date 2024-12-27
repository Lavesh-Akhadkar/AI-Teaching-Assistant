from swarmauri.llms.concrete.GroqAIAudio import GroqAIAudio
import os
from dotenv import load_dotenv

load_dotenv()


def transcribe_audio(audio_path="audio/audio.mp3"):
    llm = GroqAIAudio(api_key=os.environ.get("GROQ_API_KEY"))

    text = llm.predict(audio_path, task="transcription")

    return text
