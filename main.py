import os
from pathlib import Path
import sys

def merge_ts_like_files(folder_path, extension, output_filename):
    folder = Path(folder_path)
    if not folder.is_dir():
        print("Invalid folder path.")
        return

    # Normalize extension (e.g., .TS -> .ts)
    extension = extension.lower().lstrip('.')
    output_file = folder / output_filename

    # Find all matching files and sort them by name
    video_files = sorted(folder.glob(f'*.{extension}'))

    if not video_files:
        print(f"No .{extension} files found in {folder}")
        return

    with open(output_file, 'wb') as outfile:
        for file in video_files:
            print(f"Adding: {file.name}")
            with open(file, 'rb') as f:
                outfile.write(f.read())

    print(f"\n✅ Merged {len(video_files)} files into {output_file}")

if __name__ == '__main__':
    folder = input("Enter path to folder containing split video files: ").strip('"')
    ext = input("Enter the file extension (e.g., ts, mts, m2ts, mod): ").strip().lower()
    out = input("Enter output filename (e.g., merged.ts): ").strip()
    merge_ts_like_files(folder, ext, out)
