"""File operations."""
import datetime


def get_default_filename(extension: str) -> str:
    """Generate a default filename with a timestamp and the given extension."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{timestamp}_output.{extension}"


def save_transcript_to_file(transcript: str, file_path: str) -> None:
    """Save the transcript to a text file."""
    with open(file_path, "w", encoding="utf-8") as transcript_file:
        transcript_file.write(transcript)
