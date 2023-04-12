"""Test the youtube_dl module"""
import os

from app.youtube_dl import download_video


def test_download_video(tmpdir):
    """Test that the download_video function downloads a video"""
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    tmpdir.mkdir("outputs")
    downloaded_file = download_video(url)
    assert os.path.exists(downloaded_file)
