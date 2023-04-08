"""Main entry point for the application."""

from pathlib import Path

from .app.whispercc import WhisperTranscriber
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

    print_hello_world()

    _audio_file = Path(
        "/Users/seandearnaley/Documents/GitHub/youtube-2-whisper-experiments/samples/George_W_Bush_Columbia_FINAL.ogg"  # pylint: disable=line-too-long  # noqa: E501
    )
    transcriber = WhisperTranscriber("tiny.en")
    transcription = transcriber.transcribe_audio(_audio_file)
    print(transcription)
