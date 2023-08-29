# README.md

---

## File Organizer Script

This Python script helps in organizing your files by their types and their respective timestamps. It's perfect for those who have cluttered directories and want to bring order to their digital life.

### Features:

1. **Sort By File Type**: The script classifies files into three main categories:
   - Documents (e.g., `.doc`, `.docx`, `.xls`, `.xlsx`, `.csv`, `.ppt`, `.pptx`, `.pdf`)
   - Photos (e.g., `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`)
   - Videos (e.g., `.mp4`, `.mkv`, `.flv`, `.avi`, `.mov`, `.wmv`)

2. **Timestamp Based Sorting for Photos and Videos**: Within the categories of photos and videos, the script further organizes them based on the most recent timestamp (either creation or modification date).

### How to Use:

1. **Clone/Download the Script**: First, get the script onto your local machine.
2. **Command Line Arguments**: The script expects two mandatory command line arguments:
   - `--source`: The source directory where the files are currently located.
   - `--dest`: The destination directory where you want the organized files to be moved to.
3. **Run the Script**: Navigate to the directory containing the script and run:
   ```bash
   python file_organizer.py --source <path_to_source_directory> --dest <path_to_destination_directory>
   ```
   Replace `<path_to_source_directory>` with your source directory path and `<path_to_destination_directory>` with your desired destination directory path.

### Example:

Let's say you have a folder `Downloads` which is cluttered, and you want to organize the files into a folder named `OrganizedFiles`. You can run:

```bash
python file_organizer.py --source Downloads --dest OrganizedFiles
```

After running the script, the `OrganizedFiles` directory will have sub-directories named `doc`, `photo`, and `video`. Inside `photo` and `video`, there will be further directories based on dates.

### Note:

- Files with extensions not recognized by the script will remain in the source directory.
- Ensure you have necessary permissions to move files from the source directory to the destination directory.

---

Hope this script makes your digital life a tad bit more organized! Happy sorting!
