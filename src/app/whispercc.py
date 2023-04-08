"""WhisperCC binding module"""
from __future__ import annotations

from pathlib import Path

import ffmpeg
import numpy as np
from whispercpp import Whisper

SAMPLE_RATE = 16000


class WhisperTranscriber:
    """Transcribes audio using the Whisper model"""

    def __init__(self, model: str) -> None:
        self.whisper = Whisper.from_pretrained(model)

    def transcribe_audio(self, audio_file: Path) -> str:
        """Transcribes audio from a file"""
        audio_data = self._load_audio(audio_file)
        transcription = self.whisper.transcribe(audio_data)
        return transcription

    def _load_audio(self, audio_file: Path) -> np.ndarray:
        audio_data = self._decode_audio(audio_file)
        audio_array = self._convert_to_float_array(audio_data)
        return audio_array

    def _decode_audio(self, audio_file: Path) -> bytes:
        try:
            audio_data, _ = (
                ffmpeg.input(str(audio_file), threads=0)
                .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=SAMPLE_RATE)
                .run(
                    cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True
                )
            )
            return audio_data
        except ffmpeg.Error as ffmpeg_err:
            raise RuntimeError(
                f"Failed to load audio: {ffmpeg_err.stderr.decode()}"
            ) from ffmpeg_err

    def _convert_to_float_array(self, audio_data: bytes) -> np.ndarray:
        int_array = np.frombuffer(audio_data, np.int16).flatten()
        float_array = int_array.astype(np.float32) / 32768.0
        return float_array
