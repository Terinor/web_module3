import os


def create_list_of_files(file_path):
    output_file_path = os.path.join(file_path, "file_list.txt")
    items_list = os.walk(file_path)
    with open(output_file_path, "w") as file:
        for items in items_list:
            file.write("Address:" + str(items[0]) + "\n")
            file.write("Folders:" + str(items[1]) + "\n")
            file.write("Files:" + str(items[2]) + "\n" + "\n")
