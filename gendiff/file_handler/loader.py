import os


def get_data_from_file(file_path):
    with open(file_path) as file_data:
        return file_data.read()


def get_file_extension(file_path):
    full_name = os.path.basename(file_path)
    extension = full_name.split('.')[1].lower()
    return extension
