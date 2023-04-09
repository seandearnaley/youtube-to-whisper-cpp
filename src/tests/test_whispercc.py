"""Test the WhisperTranscriber class."""
from pathlib import Path
from unittest.mock import MagicMock

from src.app.whispercc import WhisperTranscriber


def test_whisper_transcriber():
    """Test that the WhisperTranscriber class initializes correctly"""
    model = "tiny.en"
    whisper_transcriber = WhisperTranscriber(model)
    assert whisper_transcriber.whisper is not None


def test_transcribe_audio(mocker):
    """Test that the transcribe_audio function calls the transcribe method"""
    audio_file = Path("samples/jfk.wav")
    model = "tiny.en"
    mock_transcribe = MagicMock()
    mocker.patch("whispercpp.Whisper.transcribe", mock_transcribe)
    whisper_transcriber = WhisperTranscriber(model)
    whisper_transcriber.transcribe_audio(audio_file)
    assert mock_transcribe.called
