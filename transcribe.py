import whisper
import json
import os

def tts():

    audio = whisper.load_audio("audio/audio.mp3")

    model = whisper.load_model("tiny", device="cpu")
    result = whisper.transcribe(model, audio, language="en")

    #if transcript folder doesn't exist, create it
    try:
        os.mkdir("transcript")
    except:
        pass

    with open("transcript/transcript.json", "w") as f:
        f.write(json.dumps(result, indent=2, ensure_ascii=False))


def get_transcript():
    with open("transcript/transcript.json", "r") as f:
        data = json.load(f)
    transcript = data["text"]
    return transcript

