import os
import re


def normalize(s):
    translit_dict = {
        ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'h', ord('д'): 'd',
        ord('е'): 'e', ord('є'): 'ie', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y',
        ord('і'): 'i', ord('ї'): 'i', ord('й'): 'i', ord('к'): 'k', ord('л'): 'l',
        ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
        ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh',
        ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ь'): '',
        ord('ю'): 'iu', ord('я'): 'ia', ord('ы'): 'y', ord('ъ'): '', ord('ё'): 'e',
        ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'H', ord('Д'): 'D',
        ord('Е'): 'E', ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y',
        ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L',
        ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R',
        ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh',
        ord('Ц'): 'Ts', ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ь'): '',
        ord('Ю'): 'Yu', ord('Я'): 'Ya', ord('Ы'): 'Y', ord('Ъ'): '', ord('Ё'): 'E'
    }

    normalized = s.translate(translit_dict)
    normalized = re.sub(r'[^A-Za-z0-9.]', '_', normalized)
    return normalized


def normalize_objects_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            new_name = normalize(folder_name)
            new_path = os.path.join(root, new_name)

            if new_name != folder_name:
                os.rename(folder_path, new_path)

        for file_name in files:
            file_path = os.path.join(root, file_name)
            new_name = normalize(file_name)
            new_path = os.path.join(root, new_name)

            if new_name != file_name:
                os.rename(file_path, new_path)
