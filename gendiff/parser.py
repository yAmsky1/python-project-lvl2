import json
import os
import yaml


ERROR = 'Invalid file type (The program only supports *.json and *.yaml/*.yml)'


def get_data_from_file(file_path):
    with open(file_path) as file_data:
        return file_data.read()


def get_file_extension(file_path):
    full_name = os.path.basename(file_path)
    extension = full_name.split('.')[1].lower()
    return extension


def parse_file(file_path):
    file_types = {
        "json": json.loads,
        "yml": yaml.safe_load,
        "yaml": yaml.safe_load
    }
    file_data = get_data_from_file(file_path)
    file_extension = get_file_extension(file_path)
    parser = file_types.get(file_extension)
    return parser(file_data) if parser else ERROR
