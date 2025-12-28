# Delete Duplicate Images
A fast, offline CLI tool to find and remove visually duplicate images.

## Overview
This Python script scans a specified directory for duplicate images and removes them automatically. It utilizes the **dHash (Difference Hashing) algorithm** to detect duplicate images based on visual similarity rather than just filenames or metadata.

## Features
- **Fast Duplicate Detection**: Uses dHash to compare image similarity efficiently.
- **Batch Processing**: Scans and processes all images in the specified directory.
- **Dry Run Option**: Allows you to preview duplicates before deletion.
- **Automated Deletion**: Removes duplicate images while keeping one copy.

## Installation
Make sure you have Python installed along with the required dependencies:

```bash
pip install -r requirements.txt
```

### Option 1: Run as Python script
```bash
python imgdedup.py ./photos
```

### Option 2: Install as CLI (Linux/macOS/Windows)
```bash
pip install -e .
duplicate-image-finder ./photos --remove
```

Or install from PyPI (once released):
```bash
pip install duplicate-image-finder
duplicate-image-finder ~/Pictures --remove
```

### Option 3: Use Windows executable (Windows only)
Download `imgdedup.exe` from [releases](https://github.com/Shailesh7860/Delete-Duplicate-Images/releases) and run:
```bash
imgdedup.exe C:\Users\YourName\Pictures --remove
```

To build your own Windows .exe, see [Building from Source](#building-from-source) below.


## Usage
Run the script with the following command:

```bash
# Dry-run: preview duplicates without deleting
python imgdedup.py ./photos

# Actually remove duplicates
python imgdedup.py ./photos --remove
```

Or if installed via pip:

```bash
# Dry-run
duplicate-image-finder ./photos

# Remove duplicates
duplicate-image-finder ./photos --remove
```

### Arguments:
- `path`: Path to the folder containing images (required).
- `--dry-run`: Preview duplicates without deleting (default behavior).
- `--remove`: Actually delete duplicate images.

### Example:
```bash
# Preview duplicates in Pictures folder
python imgdedup.py ~/Pictures

# Or with installed CLI:
duplicate-image-finder ~/Pictures
```

## Example Output

Running `python imgdedup.py ./photos` on a folder with duplicates:

```
[INFO] computing image hashes...
[INFO] found 42 unique image(s)
[INFO] found 7 duplicates with hash: 3644735598476604983
[INFO] found 3 duplicates with hash: 5839229124691737244
[INFO] found 2 duplicates with hash: 1928840737112196108
```

Running with `--remove`:

```
[INFO] computing image hashes...
[INFO] found 42 unique image(s)
[INFO] removing 7 duplicates with hash: 3644735598476604983
[INFO] removing 3 duplicates with hash: 5839229124691737244
[INFO] removing 2 duplicates with hash: 1928840737112196108
```

## Dependencies
The script requires the following Python packages:
- `imutils`
- `numpy`
- `opencv-python` (cv2)
- `argparse` (built-in)

## Building from Source

### Build Windows .exe

Requires: Python 3.7+, PyInstaller

**On Windows:**
```bash
pip install PyInstaller
build_exe.bat
```

**On Linux/macOS:**
```bash
pip install PyInstaller
bash build_exe.sh
```

The executable will be created in `releases/imgdedup.exe`.

## License
This project is open-source under the MIT License.

## Roadmap

Future enhancements planned for duplicate-image-finder:

- [ ] Publish to PyPI: `pip install duplicate-image-finder`
- [ ] Create Windows executable (.exe) for non-developers
- [ ] Add hash tolerance/threshold support for similar (not identical) duplicates
- [ ] Recursive folder scanning with `--recursive` flag
- [ ] Progress bar for large image collections
- [ ] Configuration file support (.dedup.config)
- [ ] GitHub Actions for automated releases
- [ ] Performance optimizations for 10,000+ images

---

This script is a powerful tool for keeping your image collections clean and organized by eliminating duplicate files. Feel free to contribute or enhance its functionality!

