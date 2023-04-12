"""WhisperCC binding module"""
from __future__ import annotations

from pathlib import Path

from whispercpp import Whisper

from .audio_tools import NdArray, convert_to_float_array, decode_audio


class WhisperTranscriber:
    """WhisperCC transcriber"""

    def __init__(self, model: str) -> None:
        """Initialize the transcriber"""
        self.whisper = Whisper.from_pretrained(model)

    def transcribe_audio(self, audio_file: Path) -> str:
        """Transcribe audio from a file"""
        audio_data = self._load_audio(audio_file)
        transcription = self.whisper.transcribe(audio_data)
        return transcription

    def _load_audio(self, audio_file: Path) -> NdArray:
        """Load audio from a file"""
        audio_data = decode_audio(audio_file)
        audio_array = convert_to_float_array(audio_data)
        return audio_array
