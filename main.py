import os
from pathlib import Path
from tkinter import Tk, filedialog
from tkinter.messagebox import showinfo

def merge_selected_files(file_paths, output_filename='merged_output.ts'):
    if not file_paths:
        showinfo("No Files Selected", "You did not select any files.")
        return

    # Convert to Path objects and sort
    files = sorted(Path(fp) for fp in file_paths)

    # Use the folder of the first file as the output location
    output_file = files[0].parent / output_filename

    with open(output_file, 'wb') as outfile:
        for file in files:
            print(f"Merging: {file.name}")
            with open(file, 'rb') as f:
                outfile.write(f.read())

    showinfo("Merge Complete", f"Merged {len(files)} files into:\n{output_file}")

def choose_files_and_merge():
    root = Tk()
    root.withdraw()  # Hide main tkinter window

    file_paths = filedialog.askopenfilenames(
        title="Select Video Files to Merge",
        filetypes=[("Video files", "*.ts *.mts *.m2ts *.mod"), ("All files", "*.*")]
    )

    merge_selected_files(file_paths)

if __name__ == '__main__':
    choose_files_and_merge()
