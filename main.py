import subprocess
import time
from pathlib import Path
from tkinter import Tk, filedialog

def merge_selected_files(file_paths):
    if not file_paths:
        print("No files selected. Exiting.")
        return

    files = sorted(Path(fp) for fp in file_paths)
    input_extension = files[0].suffix.lower()
    default_filename = f"merged_videos{input_extension}"
    initial_dir = files[0].parent

    # Ask for output file path
    root = Tk()
    root.withdraw()
    output_path = filedialog.asksaveasfilename(
        title="Save Merged File As",
        defaultextension=input_extension,
        initialdir=initial_dir,
        initialfile=default_filename,
        filetypes=[(f"{input_extension.upper()} Video", f"*{input_extension}")]
    )
    root.destroy()

    if not output_path:
        print("No output file selected. Exiting.")
        return

    output_file = Path(output_path)
    total_size = sum(f.stat().st_size for f in files)
    written = 0
    last_update_time = time.time()
    CHUNK_SIZE = 64 * 1024 * 1024  # First number is megabite size for each chunk.
    try:
        with open(output_file, 'wb') as outfile:
            for file in files:
                print(f"\nMerging: {file.name}")
                with open(file, 'rb') as f:
                    while chunk := f.read(CHUNK_SIZE):
                        outfile.write(chunk)
                        written += len(chunk)
                        percent = (written / total_size) * 100
                        print(f"Progress: {percent:.2f}%", end='\r')

        print("\nMerge complete!")
    except Exception as e:
        print(f"\nError during merging: {e}")
        return

    # Ask user if they want to open folder
    open_folder = input(f"\nOpen output folder? (y/n): ").strip().lower()
    if open_folder == 'y':
        subprocess.run(['explorer', str(output_file.parent)])

def choose_files_and_merge():
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Select Video Files to Merge",
        filetypes=[("Video files", "*.ts *.mts *.m2ts *.mod"), ("All files", "*.*")]
    )
    root.destroy()

    merge_selected_files(file_paths)

if __name__ == '__main__':
    choose_files_and_merge()
