import os
import sys
import shutil
from datetime import datetime
import argparse

def determine_file_type_timestamp(file_path):
    # File extensions for each type
    doc_extensions = ['.doc', '.docx','.xls', '.xlsx', '.csv', '.ppt', '.pptx','.pdf']
    picture_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    video_extensions = ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv']
    ext = os.path.splitext(file_path)[1].lower()

    created_time = os.path.getctime(file_path)
    modified_time = os.path.getmtime(file_path)
    
    recent_time = max(created_time, modified_time)
    created_date = datetime.fromtimestamp(recent_time).strftime('%Y-%m-%d')

    if ext in doc_extensions:
        file_type = 'doc'
    elif ext in picture_extensions:
        file_type =  'photo'
    elif ext in video_extensions:
        file_type =  'video'
    else:
        file_type =  ''
    
    return file_type, created_date

def move_file(source_path, destination_folder, date_folder, delete):
    # Get file type and current date
    file_type, created_date = determine_file_type_timestamp(source_path)
    
    if file_type:
        # Create necessary directories
        if date_folder :
            dest_dir = os.path.join(destination_folder, file_type, created_date)
        else:    
            dest_dir = os.path.join(destination_folder, file_type)
        os.makedirs(dest_dir, exist_ok=True)
        
        # Move the file
        dest_path = os.path.join(dest_dir, os.path.basename(source_path))
        if delete:
            shutil.move(source_path, dest_path)
        else:
            shutil.copy(source_path,dest_path)
            
def search_and_move_files(root_dir, destination_folder,date_folder, delete):
    print(f'source: {root_dir}, dest: {destination_folder}')
    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            source_path = os.path.join(foldername, filename)
            print(f'processing: {source_path}')
            move_file(source_path, destination_folder,date_folder, delete)

def get_folder_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024)  # converting bytes to MB

def print_destination_folder_sizes(destination_folder):
    main_folder_size = get_folder_size(destination_folder)
    print(f"Total size of {destination_folder}: {main_folder_size:.2f} MB")

    for folder in ["doc", "photo", "video"]:
        folder_path = os.path.join(destination_folder, folder)
        if os.path.exists(folder_path):
            folder_size = get_folder_size(folder_path)
            print(f"Size of {folder}: {folder_size:.2f} MB")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="source and dest folders")
    parser.add_argument("--source", type=str, required=True, help="source folder")
    parser.add_argument("--dest", type=str, required=True, help="dest")
    parser.add_argument("--date_folder", type=bool, required=False, help="date_folder", default=True)
    parser.add_argument("--delete", type=bool, required=False, help="delete", default=False)
    args = parser.parse_args()
    search_and_move_files(args.source, args.dest,args.date_folder, args.delete)
    print_destination_folder_sizes(args.dest)
