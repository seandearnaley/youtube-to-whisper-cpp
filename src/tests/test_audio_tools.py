"""Test the audio_tools module"""
import os
from pathlib import Path

import numpy as np

from src.app.audio_tools import (
    convert_audio_format,
    convert_to_float_array,
    decode_audio,
)


def test_decode_audio():
    """Test that the decode_audio function returns a bytes object"""
    audio_file = Path("samples/jfk.wav")
    decoded_audio = decode_audio(audio_file)
    assert isinstance(decoded_audio, bytes)


def test_convert_to_float_array():
    """Test that the convert_to_float_array function returns a numpy array"""
    audio_data = b"\x00\x00\x00\x00"
    float_array = convert_to_float_array(audio_data)
    assert isinstance(float_array, np.ndarray)
    assert float_array.dtype == np.float32


def test_convert_audio_format(tmpdir):
    """Test that the convert_audio_format function returns a file path"""
    input_file = "samples/jfk.wav"
    output_file_name = "output.mp3"
    output_dir = tmpdir.mkdir("outputs")
    output_file_path = os.path.join(output_dir, output_file_name)
    converted_file = convert_audio_format(input_file, output_file_path, "mp3")
    assert os.path.exists(converted_file)
