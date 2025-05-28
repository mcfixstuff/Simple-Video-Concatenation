import os
import re
from pathlib import Path
from tkinter import Tk, filedialog
from tkinter.messagebox import showinfo

# Supported video file extensions
VIDEO_EXTS = ['.ts', '.mts', '.m2ts', '.mod']

def is_incremental_name(filename):
    """Check if a file has an incremental-style name (e.g., moviea, movieb, 0001, 0002)."""
    stem = filename.stem.lower()
    return bool(re.search(r'\d+$', stem) or re.search(r'[a-z]+$', stem))

def merge_files(folder_path: Path, output_filename='merged_output.ts'):
    # Filter video files with incremental-style names
    video_files = [
        f for f in folder_path.iterdir()
        if f.suffix.lower() in VIDEO_EXTS and is_incremental_name(f)
    ]

    if not video_files:
        showinfo("No Files Found", "No matching incremental video files found.")
        return

    # Sort files alphabetically (which works for names like 0001, 0002 or moviea, movieb)
    video_files.sort()

    output_file = folder_path / output_filename

    with open(output_file, 'wb') as outfile:
        for file in video_files:
            print(f"Merging: {file.name}")
            with open(file, 'rb') as f:
                outfile.write(f.read())

    showinfo("Merge Complete", f"Merged {len(video_files)} files into:\n{output_file}")

def choose_folder_and_merge():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    folder_selected = filedialog.askdirectory(title="Select Folder Containing Video Segments")

    if not folder_selected:
        showinfo("Cancelled", "No folder selected.")
        return

    merge_files(Path(folder_selected))

if __name__ == '__main__':
    choose_folder_and_merge()
