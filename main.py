import os
from time import perf_counter
from listing_files import create_list_of_files
from clean_empty import delete_empty_folders
from normalize import normalize_objects_in_directory
from sort_refactor import process_file
from concurrent.futures import ThreadPoolExecutor


def sort_directory(directory_path, categories):
    start_time = perf_counter()
    category_directories = [os.path.join(directory_path, cat) for cat in categories.keys()]
    normalize_objects_in_directory(directory_path)

    with ThreadPoolExecutor(max_workers=1000) as executor:
        for root, folders, files in os.walk(directory_path, topdown=True):
            if any(root.startswith(cat_dir) for cat_dir in category_directories):
                continue

            for file_name in files:
                if file_name == "file_list.txt":
                    continue

                file_path = os.path.join(root, file_name)
                executor.submit(process_file, file_path, file_name, directory_path, categories)

    delete_empty_folders(directory_path)
    create_list_of_files(directory_path)

    end_time = perf_counter()
    elapsed_time = end_time - start_time
    print(f"Час виконання програми: {elapsed_time} секунд")

if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print(f"Usage: python sort.py <directory_path>")
    # else:
        path_to_directory = r'D:\хлам'
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
                'database': ('.mdb', '.accdb', '.xlsm', '.xlsx', '.xls', '.db', '.bsdu', '.ims'),
                'rza_images': ('.teax', '.pcmp'),
                'go_it': ('.zahruzheno', '.css', '.html'),
                'torrents': ('.torrent',)
            }
            sort_directory(path_to_directory, folders_categories)
