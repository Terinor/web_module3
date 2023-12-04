import os
import shutil
# import re
import sys
from listing_files import create_list_of_files
from renaming_files import rename_file_with_folder_name
from clean_empty import delete_empty_folders
from normalize import normalize_objects_in_directory
from sort_refactor import process_file


def sort_directory(directory_path, categories):
    normalize_objects_in_directory(directory_path)

    for root, folders, files in os.walk(directory_path):
        if os.path.basename(root) not in categories.keys():
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if file_name == "file_list.txt":
                    os.remove(file_path)
                    continue
                process_file(file_path, file_name, directory_path, categories)

    delete_empty_folders(directory_path)
    create_list_of_files(directory_path)


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print(f"Usage: python sort.py <directory_path>")
    # else:
        path_to_directory = r'C:\Users\razie\Downloads'
        if not os.path.isdir(path_to_directory):
            print("Invalid directory path.")
        else:

            folders_categories = {
                'images': ('.jpg', '.png', '.jpeg', '.svg'),
                'video': ('.avi', '.mp4', '.mov', '.mkv'),
                'audio': ('.mp3', '.ogg', '.wav', '.amr'),
                'documents': ('.doc', '.docx', '.docm', '.txt', '.pdf', '.pptx'),
                'archives': ('.zip', '.gz', '.tar', '.rar', '.7z', '.iso'),
                '3Dmodels': ('.stl',),
                'applications': ('.exe', '.bin', '.msi'),
                'database': ('.mdb', '.accdb', '.xlsm', '.xlsx', '.xls'),
                'torrents': ('.torrent',)
            }
            sort_directory(path_to_directory, folders_categories)
