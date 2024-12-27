from pytubefix import YouTube
import os
from transcribe import transcribe_audio


def download_audio(video_url):
    yt = YouTube(video_url, use_po_token=True)

    try:
        os.mkdir("audio")
    except:
        pass

    os.system("rm -rf audio/*")
    yt.streams.filter(only_audio=True).first().download("audio", "audio.mp3")

def video_to_transcript(video_url):
    download_audio(video_url)
    return transcribe_audio()
