# YouTube to Whisper CPP Transcriber

This project is a simple YouTube transcriber that transcribes YouTube videos using the Whisper CPP library. No GPU required, no calls to OpenAI. The transcriptions are generated from the audio of the YouTube video.

It uses [whisper.cpp](https://github.com/ggerganov/whisper.cpp) for speech recognition (with python bindings by [aarnphm](https://github.com/aarnphm/whispercpp)) and [pytube](https://pytube.io/en/latest/) for downloading YouTube videos. It also uses [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) for audio processing.  You will need to follow their installation instructions to install the necessary dependencies.  (Note: [ffmpeg](http://www.ffmpeg.org/) must be installed and the `ffmpeg` executable must be in your `PATH` environment variable.)

## Main Scripts

### src/app/audio_tools.py

This script contains audio processing tools for decoding, converting, and handling audio files. It uses the `ffmpeg-python` library for audio processing.

### src/app/whispercc.py

This script contains the `WhisperTranscriber` class, which is responsible for transcribing audio files using the Whisper CPP library.

### src/app/youtube_dl.py

This script downloads a YouTube video and converts it to an audio file using the `pytube` library.

### src/main.py

This script is the main entry point for the application. It downloads a YouTube video, converts it to an audio file, and transcribes the audio using the `WhisperTranscriber` class.

## Installation

1. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already.
2. Clone the repository and navigate to the project directory.
3. I suggest using python 3.10.11 `poetry env use 3.10.11`, whisper cpp bindings will need wheels for your architecture. See [docs](https://github.com/aarnphm/whispercpp)
4. Run `poetry install` to install the dependencies.

## Usage

1. Set up the environment variables by copying the `.env.example` file to a new file named `.env` and modifying the values as needed.
2. Run the application using `poetry run transcribe <url> [<output_file_name>] [<transcript_file_path>]`. (note the output_file_name is the wav from the dl)

Alternative Usage: `python3 src/main.py <url> [<output_file_name>] [<transcript_file_path>]`

## Contributing

Please follow the standard Git workflow for contributing to this project:

1. Fork the repository and create a new branch for your feature or bugfix.
2. Make your changes and commit them to your branch.
3. Push your changes to your fork and create a pull request against the main repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
