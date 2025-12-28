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

## Usage
Run the script with the following command:

```bash
python imgdedup.py -d "path_to_images_folder" -r 1
```

### Arguments:
- `-d` or `--dataset`: Path to the folder containing images.
- `-r` or `--remove`: Set to `1` to delete duplicates or `0` for a dry run (preview only).

### Example:
```bash
python imgdedup.py -d "C:/Users/YourName/Pictures" -r 1
```
This will scan the `Pictures` folder and delete duplicate images.

## Dependencies
The script requires the following Python packages:
- `imutils`
- `numpy`
- `argparse`
- `cv2` (OpenCV)
- `os`

## License
This project is open-source under the MIT License.

---

This script is a powerful tool for keeping your image collections clean and organized by eliminating duplicate files. Feel free to contribute or enhance its functionality!

