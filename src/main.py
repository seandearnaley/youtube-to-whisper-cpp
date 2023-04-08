"""Main entry point for the application."""
import sys
from pathlib import Path

from .app.whispercc import WhisperTranscriber
from .app.youtube_dl import convert_audio_to_wav, download_video
from .config import ConfigLoader
from .debug_tools import Debugger, DebugOptions
from .log_tools import Logger

app_logger = Logger.get_app_logger()


def print_hello_world() -> None:
    """Print hello world."""
    print("Hello, World!")


def load_config() -> DebugOptions:
    """Load configuration and return an instance of DebugOptions."""
    config = ConfigLoader.get_config()
    return DebugOptions(
        flag=config["ATTACH_DEBUGGER"],
        wait_for_client=config["WAIT_FOR_CLIENT"],
        host=config["DEBUGPY_HOST"],
        port=config["DEFAULT_DEBUG_PORT"],
    )


def main() -> None:
    """Main method."""
    app_logger.info("Loading")

    # Set up the debugger if enabled in the configuration
    debug_options = load_config()
    Debugger.setup_debugpy(app_logger, debug_options)

    url = "https://www.youtube.com/watch?v=iq9a-cP0T2g&t=1969s"
    output_file = "h3h3.wav"

    downloaded_file = download_video(url)
    if downloaded_file is None:
        sys.exit(2)

    converted_file = convert_audio_to_wav(downloaded_file, output_file)
    if not converted_file:
        sys.exit(3)

    _audio_file = Path(converted_file)
    transcriber = WhisperTranscriber("tiny.en")
    transcription = transcriber.transcribe_audio(_audio_file)
    print(transcription)
