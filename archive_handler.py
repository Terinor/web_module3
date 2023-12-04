import shutil
import os
import py7zr


def handle_archived_file(file_path, file_name, file_extension, directory_path):
    dest_folder = 'archives'
    archive_dest_folder_path = prepare_destination_for_archive(file_name, directory_path, dest_folder)

    if file_extension == '.7z':
        # Обробка архівів .7z
        unpack_7z_archive(file_path, archive_dest_folder_path)
    elif file_extension in shutil.get_unpack_formats():
        # Обробка інших підтримуваних форматів
        try:
            shutil.unpack_archive(file_path, archive_dest_folder_path)
            os.remove(file_path)
        except shutil.ReadError:
            # Якщо архів не може бути розпакований
            move_to_destination(file_path, archive_dest_folder_path)
    else:
        # Переміщення архівів, які не підтримуються
        move_to_destination(file_path, archive_dest_folder_path)


def prepare_destination_for_archive(file_name, directory_path, dest_folder):
    # Функція для підготовки місця призначення
    dest_folder_path = os.path.join(directory_path, dest_folder)
    os.makedirs(dest_folder_path, exist_ok=True)
    return dest_folder_path


def unpack_7z_archive(file_path, dest_path):
    # Функція для розпакування архівів .7z
    with py7zr.SevenZipFile(file_path, mode='r') as z:
        z.extractall(path=dest_path)
    os.remove(file_path)


def move_to_destination(file_path, dest_folder_path):
    # Функція для переміщення файлу
    dest_file_path = os.path.join(dest_folder_path, os.path.basename(file_path))
    shutil.move(file_path, dest_file_path)
