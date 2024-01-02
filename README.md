# MP3 Silence Detection and Concatenation Script

## Overview
This Python script utilizes the `pydub` library to analyze an MP3 file, detect silence, and export non-silent segments as individual WAV files. 
Additionally, it concatenates the non-silent segments into a new MP3 file.

## Requirements
- Python 3.x
- pydub library (install using `pip install pydub`)
- ffmpeg, added to your path environment

## Usage
Run the script from the command line, providing the path to the MP3 file as a command-line argument.

```bash
python script.py path/to/your/file.mp3
