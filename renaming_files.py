import os


def rename_file_with_folder_name(file_path):
    folder_path = os.path.dirname(file_path)
    folder_name = os.path.basename(folder_path)
    file_name = os.path.basename(file_path)

    new_name = f"{folder_name}_{file_name}"
    new_path = os.path.join(folder_path, new_name)

    os.rename(file_path, new_path)
    return new_path, new_name

