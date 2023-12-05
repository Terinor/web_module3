import os
import shutil
from renaming_files import rename_file_with_folder_name
from archive_handler import handle_archived_file


def process_file(file_path, file_name, directory_path, categories):
    file_extension = os.path.splitext(file_name)[1].lower()

    if file_extension == '.tmp':
        os.remove(file_path)
        return

    archive_extensions = categories.get('archives', [])
    if file_extension in archive_extensions:
        handle_archived_file(file_path, file_name, file_extension, directory_path)
    else:
        handle_regular_file(file_path, file_extension, directory_path, categories)


def handle_regular_file(file_path, file_extension, directory_path, categories):
    for category, extensions in categories.items():
        if file_extension in extensions:
            dest_folder_path = os.path.join(directory_path, category)
            os.makedirs(dest_folder_path, exist_ok=True)
            move_to_destination(file_path, dest_folder_path)
            return

    #print(f"Unknown file extension: {file_path}")


def move_to_destination(file_path, dest_folder_path):
    file_path, file_name = rename_file_with_folder_name(file_path)
    dest_file_path = os.path.join(dest_folder_path, file_name)
    if os.path.isfile(dest_file_path):
        existing_file_stat = os.stat(dest_file_path)
        current_file_stat = os.stat(file_path)
        if current_file_stat.st_ctime > existing_file_stat.st_ctime:
            shutil.move(file_path, dest_file_path)
    else:
        shutil.move(file_path, dest_file_path)
