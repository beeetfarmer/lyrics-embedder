# Lyrics Embedder

A simple Python tool that embeds lyrics from .lrc files into your music files. This script automatically scans your music folders and adds lyrics as metadata to your audio files.

## Features

- Supports multiple audio formats: MP3, FLAC, M4A, and OGG
- Works recursively through folders and subfolders
- Simple command-line interface
- Visual feedback with emoji indicators

## Requirements

- Python 3.6 or higher
- Mutagen library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/beeetfarmer/lyrics-embedder.git
   cd lyrics-embedder
   ```

2. Install the required dependencies:
   ```
   pip install mutagen
   ```

## Usage

### Basic Usage

Simply run the script and follow the prompts:

```
python main.py
```

The script will ask for a folder path and then confirm before starting the embedding process.

### Command-Line Arguments

You can also specify the folder path directly as an argument:

```
python main.py "/path/to/your/music"
```

## How It Works

1. The script scans for audio files with extensions .mp3, .flac, .m4a, or .ogg
2. For each audio file, it looks for a matching .lrc file with the same name
3. If a matching lyrics file is found, the lyrics are embedded into the audio file's metadata
4. The process is repeated for all subfolders if recursive mode is enabled

## File Matching

For an audio file named `song.mp3`, the script will look for a lyrics file named `song.lrc` in the same folder.

## Notes

- The script preserves any timestamps in the .lrc files
- Original audio files are modified - make a backup if needed
- The script will show a warning for audio files with no matching lyrics files
