"""Download a YouTube video and convert it to WAV format."""
import os
from typing import Optional

import ffmpeg
from pytube import YouTube


def download_video(url: str) -> Optional[str]:
    """Download a YouTube video and return the path to the downloaded file."""
    try:
        yt_dl = YouTube(url)
        stream = yt_dl.streams.filter(only_audio=True).first()
        return stream.download()
    except Exception as err:  # pylint: disable=broad-except
        print(f"Error downloading video: {err}")
        return None


def convert_audio_to_wav(input_file: str, output_file: str) -> str:
    """Convert an audio file to WAV format."""
    try:
        audio = ffmpeg.input(input_file)
        audio = audio.output(output_file, format="wav")
        audio.run()
        return os.path.abspath(output_file)
    except Exception as err:  # pylint: disable=broad-except
        print(f"Error converting audio to WAV: {err}")
        return ""
