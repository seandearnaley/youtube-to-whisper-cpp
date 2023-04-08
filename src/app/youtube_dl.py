"""Download a YouTube video and convert it to WAV format."""
import os
from typing import Optional

from pytube import YouTube


def download_video(url: str) -> Optional[str]:
    """Download a YouTube video."""
    try:
        yt_dl = YouTube(url)
        stream = yt_dl.streams.filter(only_audio=True).first()
        return stream.download(output_path=os.path.join(os.getcwd(), "outputs"))
    except Exception as err:  # pylint: disable=broad-except
        print(f"Error downloading video: {err}")
        return None
