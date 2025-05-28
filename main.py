import subprocess
from pathlib import Path
from tkinter import Tk, filedialog, messagebox

def merge_selected_files(file_paths):
    if not file_paths:
        messagebox.showinfo("No Files Selected", "You did not select any files.")
        return

    # Convert to Path objects and sort
    files = sorted(Path(fp) for fp in file_paths)
    input_extension = files[0].suffix.lower()
    default_filename = f"merged_videos{input_extension}"
    initial_dir = files[0].parent

    # Ask user where to save the output file
    output_path = filedialog.asksaveasfilename(
        title="Save Merged File As",
        defaultextension=input_extension,
        initialdir=initial_dir,
        initialfile=default_filename,
        filetypes=[(f"{input_extension.upper()} Video", f"*{input_extension}")]
    )

    if not output_path:
        messagebox.showinfo("Cancelled", "No output file was selected.")
        return

    output_file = Path(output_path)

    with open(output_file, 'wb') as outfile:
        for file in files:
            print(f"Merging: {file.name}")
            with open(file, 'rb') as f:
                outfile.write(f.read())

    # Ask if user wants to open folder
    open_folder = messagebox.askyesno(
        "Merge Complete",
        f"Merged {len(files)} files into:\n{output_file.name}\n\nOpen output folder?"
    )

    if open_folder:
        subprocess.run(['explorer', str(output_file.parent)])

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
