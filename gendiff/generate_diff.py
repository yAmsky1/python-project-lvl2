import json
import yaml
from gendiff.formatters.formatter import get_formatter
from gendiff.tags import ADDED, REMOVED, UNCHANGED, CHANGED, NESTED


def generate_diff(file_path1: str, file_path2: str, form='stylish') -> str:
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    diff = check_diff(file1, file2)
    return get_formatter(diff, form)


def parse_file(file_path):
    file_types = {
        "json": json.load,
        "yml": yaml.safe_load,
        "yaml": yaml.safe_load
    }
    for file_type in file_types:
        if file_path.endswith(file_type):
            return file_types.get(file_type)(open(file_path))


def check_diff(file1, file2):
    diff = {}
    added_keys = list(file2.keys() - file1.keys())
    removed_keys = list(file1.keys() - file2.keys())
    common_keys = list(file1.keys() & file2.keys())
    for key in added_keys:
        diff[key] = [ADDED, file2.get(key)]
    for key in removed_keys:
        diff[key] = [REMOVED, file1.get(key)]
    for key in common_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = [NESTED, check_diff(value1, value2)]
        elif value1 == value2:
            diff[key] = [UNCHANGED, value1]
        else:
            diff[key] = [CHANGED, value1, value2]
    return diff
