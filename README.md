# Video File Merger

**Video File Merger** is a lightweight, portable Windows tool for quickly and safely merging split video files (such as `.TS`, `.MTS`, `.M2TS`, and `.MOD`) into one. It uses a simple graphical file selector and shows live progress updates in the terminal. No installation required.

---

## Features

- Merge video files with matching formats and incremental names (e.g., `0001.ts`, `0002.ts`, etc.)
- Compatible with formats like `.TS`, `.MTS`, `.M2TS`, `.MOD`
- Automatically detects the correct output format
- Fast merging using large 128MB blocks to reduce hard drive wear
- Live progress reporting in the terminal
- Prompts to open the output folder after completion
- No video re-encoding — 100% lossless copy

---

## How to Use

1. **Download** the latest `.exe` from the [Releases]([https://github.com/yourusername/videomerger/releases](https://github.com/mcfixstuff/Simple-Video-Concatenation/releases/tag/v0.3)) page.
2. **Run the `.exe` file** (no installation needed).
3. **Select the video files** you want to merge (use `Ctrl+Click` or `Shift+Click` to select multiple).
4. **Choose the destination and filename** for the merged video.
5. Watch progress in the terminal window.
6. When complete, you'll be prompted to open the output folder.

---

## Known Issue

**MiniDV rips `.avi` files are not fully supported.**  
When merging `.avi` files from MiniDV cameras, the resulting merged video may not show the full duration correctly in media players, even though all data is present. This is due to how `.avi` file headers and indexes work.

**Avoid using this tool for `.avi` files.**

---

## Portable & Offline

- **No installation required**
- **No internet access needed**
- Works fully offline
- Designed to be run from a USB drive or any folder

---

## Notes

- The tool does **not re-encode** video; it simply joins files together, byte-for-byte.
- Ensure the files are from the **same recording session or camera**, otherwise merged playback may fail.

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

