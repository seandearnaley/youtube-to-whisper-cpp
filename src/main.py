"""Main entry point for the application."""
import os
import sys
from pathlib import Path

from .app.audio_tools import convert_audio_format
from .app.whispercc import WhisperTranscriber
from .app.youtube_dl import download_video
from .config import ConfigLoader
from .debug_tools import Debugger, DebugOptions
from .log_tools import Logger
from .utils.file_operations import get_default_filename, save_transcript_to_file

app_logger = Logger.get_app_logger()

MODEL = "tiny.en"


def load_debugger_config() -> DebugOptions:
    """Load the configuration from the config file."""
    config = ConfigLoader.get_config()
    return DebugOptions(
        flag=config["ATTACH_DEBUGGER"],
        wait_for_client=config["WAIT_FOR_CLIENT"],
        host=config["DEBUGPY_HOST"],
        port=config["DEFAULT_DEBUG_PORT"],
    )


def do_job(url: str, output_file_name: str, transcript_file_path: str) -> None:
    """Do the job."""

    downloaded_file = download_video(url)
    if downloaded_file is None:
        sys.exit(2)

    converted_file = convert_audio_format(downloaded_file, output_file_name, "wav")
    if not converted_file:
        sys.exit(3)

    _audio_file = Path(converted_file)
    transcriber = WhisperTranscriber(MODEL)
    transcription = transcriber.transcribe_audio(_audio_file)
    print(transcription)

    save_transcript_to_file(transcription, transcript_file_path)


def main() -> None:
    """Main entry point for the application."""

    app_logger.info("Loading")

    Debugger.setup_debugpy(app_logger, load_debugger_config())

    if len(sys.argv) < 2:
        print("Usage: main.py <url> [<output_file_name>] [<transcript_file_path>]")
        sys.exit(1)

    url = sys.argv[1]
    output_file_name = (
        sys.argv[2] if len(sys.argv) >= 3 else get_default_filename("output.wav")
    )
    transcript_file_path = (
        sys.argv[3] if len(sys.argv) >= 4 else get_default_filename("transcript.txt")
    )
    transcript_file_path = os.path.join(os.getcwd(), "outputs", transcript_file_path)
    do_job(url, output_file_name, transcript_file_path)
