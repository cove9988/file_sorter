import os
import sys
import shutil
from datetime import datetime
import argparse

def determine_file_type_timestamp(file_path):
    # File extensions for each type
    doc_extensions = ['.doc', '.docx','.xls', '.xlsx', '.csv', 'ppt', 'pptx','pdf']
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

def move_file(source_path, destination_folder):
    # Get file type and current date
    file_type, created_date = determine_file_type_timestamp(source_path)
    
    if file_type:
        # Create necessary directories
        if file_type == 'doc':
            dest_dir = os.path.join(destination_folder, file_type)
        else:    
            dest_dir = os.path.join(destination_folder, file_type, created_date)
        os.makedirs(dest_dir, exist_ok=True)
        
        # Move the file
        dest_path = os.path.join(dest_dir, os.path.basename(source_path))
        shutil.move(source_path, dest_path)

def search_and_move_files(root_dir, destination_folder):
    print(f'source: {root_dir}, dest: {destination_folder}')
    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            source_path = os.path.join(foldername, filename)
            print(f'processing: {source_path}')
            move_file(source_path, destination_folder)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="source and dest folders")
    parser.add_argument("--source", type=str, required=True, help="source folder")
    parser.add_argument("--dest", type=str, required=True, help="dest")
    # parser.add_argument("--delete", type=str, required=False, help="delete")
    args = parser.parse_args()

    search_and_move_files(args.source, args.dest)
