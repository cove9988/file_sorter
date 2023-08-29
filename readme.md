### File Organizer Script

This script provides an easy way to organize files from a source folder into a centralized destination folder based on their file types. It supports sorting documents, pictures, and videos. Additionally, it can segregate these files by their creation/modification date.

---

### Features:

1. **File Type Sorting**: The script categorizes files into the following groups:
   - Documents (`doc`): `.doc`, `.docx`, `.xls`, `.xlsx`, `.csv`, `.ppt`, `.pptx`, `.pdf`
   - Pictures (`photo`): `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
   - Videos (`video`): `.mp4`, `.mkv`, `.flv`, `.avi`, `.mov`, `.wmv`

2. **Date Sorting (Optional)**: Organizes files within their type folders based on their creation or modification date.

3. **Safe Mode (Default)**: By default, the script copies files from the source to the destination. However, you can opt to move them instead.

4. **Size Summary**: At the end of the operation, the script provides a summary of the total size of the organized files and individual sizes of each category.

---

### Usage:

1. Navigate to the directory containing the script.
2. Run the script using the command:

   ```
   python [script_name].py --source [SOURCE_DIR] --dest [DEST_DIR] --date_folder [True/False] --delete [True/False]
   ```

   Replace `[script_name]` with the name of the script, `[SOURCE_DIR]` with the path to your source directory, and `[DEST_DIR]` with the path to your destination directory.

   For example:

   ```
   python file_organizer.py --source ~/Downloads --dest ~/OrganizedFiles --date_folder True --delete False
   ```

---

### Arguments:

- `--source`: Path to the source directory. *(Required)*
- `--dest`: Path to the destination directory where files will be sorted. *(Required)*
- `--date_folder`: If set to `True`, it will organize files in their type folder by date. Default is `True`. *(Optional)*
- `--delete`: If set to `True`, it will move (instead of copying) files from the source to the destination. Default is `False`. *(Optional)*

---

### Notes:

- Ensure you have the necessary permissions to read from the source directory and write to the destination directory.
- Always backup important data before using file management scripts to prevent accidental data loss.

---

### Requirements:

- Python 3.x
- Modules: `os`, `sys`, `shutil`, `datetime`, `argparse`

---

### Author:

cove9988
---

### License:

MIT

---
