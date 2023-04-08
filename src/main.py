"""Main entry point for the application."""
import sys
from pathlib import Path

from .app.audio_tools import convert_audio_format
from .app.whispercc import WhisperTranscriber
from .app.youtube_dl import download_video
from .config import ConfigLoader
from .debug_tools import Debugger, DebugOptions
from .log_tools import Logger

app_logger = Logger.get_app_logger()


def load_debugger_config() -> DebugOptions:
    """Load the configuration from the config file."""
    config = ConfigLoader.get_config()
    return DebugOptions(
        flag=config["ATTACH_DEBUGGER"],
        wait_for_client=config["WAIT_FOR_CLIENT"],
        host=config["DEBUGPY_HOST"],
        port=config["DEFAULT_DEBUG_PORT"],
    )


def do_job() -> None:
    """Do the job."""
    url = "https://www.youtube.com/watch?v=iq9a-cP0T2g&t=1969s"
    output_file = "h3h3.wav"

    downloaded_file = download_video(url)
    if downloaded_file is None:
        sys.exit(2)

    converted_file = convert_audio_format(downloaded_file, output_file, "wav")
    if not converted_file:
        sys.exit(3)

    _audio_file = Path(converted_file)
    transcriber = WhisperTranscriber("base.en")
    transcription = transcriber.transcribe_audio(_audio_file)
    print(transcription)


def main() -> None:
    """Main entry point for the application."""
    app_logger.info("Loading")

    Debugger.setup_debugpy(app_logger, load_debugger_config())

    do_job()
