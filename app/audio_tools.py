"""Audio tools for processing audio files"""
import os
from pathlib import Path

import ffmpeg
import numpy as np

SAMPLE_RATE = 16000

NdArray = np.ndarray


def decode_audio(audio_file: Path) -> bytes:
    """Decode audio from a file"""
    try:
        audio_data, _ = (
            ffmpeg.input(str(audio_file), threads=0)
            .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=SAMPLE_RATE)
            .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
        )
        return audio_data
    except ffmpeg.Error as ffmpeg_err:
        raise RuntimeError(
            f"Failed to load audio: {ffmpeg_err.stderr.decode()}"
        ) from ffmpeg_err


def convert_to_float_array(audio_data: bytes) -> NdArray:
    """Convert audio data to a float array"""
    int_array = np.frombuffer(audio_data, np.int16).flatten()
    float_array = int_array.astype(np.float32) / 32768.0
    return float_array


def convert_audio_format(
    input_file: str, output_file_name: str, audio_format: str
) -> str:
    """Convert an audio file to a different format"""
    try:
        output_file_path = os.path.join(os.getcwd(), "outputs", output_file_name)
        audio = ffmpeg.input(input_file)
        audio = audio.output(output_file_path, format=audio_format)
        audio.run()
        return output_file_path
    except Exception as err:
        raise RuntimeError(f"Error converting audio format: {err}") from err
