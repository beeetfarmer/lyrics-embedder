import os
import sys
import glob
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, USLT
from mutagen.oggvorbis import OggVorbis
from mutagen.mp4 import MP4
import re

SUPPORTED_FORMATS = (".mp3", ".flac", ".m4a", ".ogg")

def read_lyrics_file(lyrics_file):
    """Read lyrics from a .lrc file if present"""
    try:
        with open(lyrics_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
       
        # Keep the original content with timestamps
        lyrics = "".join(lines)
        return lyrics.strip()
    except Exception as e:
        print(f"Error reading {lyrics_file}: {e}")
        return None

def embed_lyrics(audio_file, lyrics):
    """Embed lyrics into the audio file"""
    ext = os.path.splitext(audio_file)[1].lower()
   
    try:
        if ext == ".mp3":
            audio = MP3(audio_file, ID3=ID3)
            audio.tags.add(USLT(text=lyrics))
            audio.save()
        elif ext == ".flac":
            audio = FLAC(audio_file)
            audio["LYRICS"] = lyrics
            audio.save()
        elif ext == ".m4a":
            audio = MP4(audio_file)
            audio["\xa9lyr"] = lyrics
            audio.save()
        elif ext == ".ogg":
            audio = OggVorbis(audio_file)
            audio["LYRICS"] = lyrics
            audio.save()
        print(f"✔ Lyrics embedded in: {audio_file}")
    except Exception as e:
        print(f"❌ Failed to embed lyrics in {audio_file}: {e}")

def process_folder(folder_path, recursive=True):
    """Process all music files in the given folder and optionally in subfolders"""
    # Process files in current folder
    for audio_file in [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(SUPPORTED_FORMATS)]:
        audio_path = os.path.join(folder_path, audio_file)
        base_name = os.path.splitext(audio_file)[0]
       
        # Check for a matching .lrc file with exact same name
        lyrics_path = os.path.join(folder_path, base_name + ".lrc")
        if os.path.exists(lyrics_path):
            lyrics = read_lyrics_file(lyrics_path)
            if lyrics:
                embed_lyrics(audio_path, lyrics)
        else:
            print(f"⚠ No lyrics found for {audio_file}")
   
    # Recursively process subfolders if enabled
    if recursive:
        for item in os.listdir(folder_path):
            subfolder = os.path.join(folder_path, item)
            if os.path.isdir(subfolder):
                print(f"\n📁 Processing subfolder: {subfolder}")
                process_folder(subfolder, recursive=True)

if __name__ == "__main__":
    # Check for command-line argument
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Enter the folder path containing your music files: ").strip()
   
    if os.path.isdir(folder):
       
        # Confirm before proceeding
        confirm = input("\nDo you want to proceed with embedding lyrics? (y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            print(f"\n📁 Starting to process: {folder}")
            process_folder(folder, recursive=True)
            print("\n✅ All done!")
        else:
            print("\n❌ Operation cancelled.")
    else:
        print(f"❌ Error: Folder '{folder}' not found!")