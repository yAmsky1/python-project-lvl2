import json
import yaml


def get_format(file_path):
    file_types = {
        "json": json.load,
        "yml": yaml.safe_load,
        "yaml": yaml.safe_load
    }
    for file_type in file_types:
        if file_path.endswith(file_type):
            return file_types.get(file_type)(open(file_path))


def generate_diff(file_path1: str, file_path2: str) -> str:
    diff = []
    file1 = get_format(file_path1)
    file2 = get_format(file_path2)
    for key in sorted(file1.keys()):
        if file1.get(key) != file2.get(key):
            diff.append(f"    - {key}: {value_formatter(file1.get(key))}")
        else:
            diff.append(f"      {key}: {value_formatter(file1.get(key))}")
    for key in sorted(file2.keys()):
        if file2.get(key) != file1.get(key):
            diff.append(f"    + {key}: {value_formatter(file2.get(key))}")
    diff = '{\n' + '\n'.join(diff) + '\n}'
    return diff


def value_formatter(value):
    if isinstance(value, bool):
        value = str(value).lower()
    return value
