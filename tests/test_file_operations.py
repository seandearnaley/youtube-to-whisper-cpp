"""Tests for file operations."""
import os
import re

from utils.file_operations import get_default_filename, save_transcript_to_file


def test_get_default_filename():
    """Test that get_default_filename returns a filename in correct format"""
    extension = "txt"
    filename = get_default_filename(extension)
    assert re.match(r"\d{8}_\d{6}_output\.txt", filename) is not None


def test_save_transcript_to_file(tmpdir):
    """Test that the save_transcript_to_file function saves a transcript to a file"""
    transcript = "This is a test transcript."
    output_dir = tmpdir.mkdir("outputs")
    file_path = os.path.join(output_dir, "transcript.txt")
    save_transcript_to_file(transcript, file_path)
    assert os.path.exists(file_path)

    with open(file_path, "r", encoding="utf-8") as transcript_file:
        saved_transcript = transcript_file.read()
    assert saved_transcript == transcript
