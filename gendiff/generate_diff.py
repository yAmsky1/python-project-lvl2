import json


def generate_diff(file_path1, file_path2):
    diff = []
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    for key in sorted(file1.keys()):
        if file1.get(key) != file2.get(key):
            diff.append(f"\t- {key}: {value_formatter(file1.get(key))}")
        else:
            diff.append(f"\t  {key}: {value_formatter(file1.get(key))}")
    for key in sorted(file2.keys()):
        if file2.get(key) != file1.get(key):
            diff.append(f"\t+ {key}: {value_formatter(file2.get(key))}")
    diff = '{\n' + '\n'.join(diff) + '\n}'
    return diff


def value_formatter(value):
    if isinstance(value, bool):
        value = str(value).lower()
    return value
