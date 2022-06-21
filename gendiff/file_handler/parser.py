import json
import yaml


def parse_file(file_data, file_extension):
    file_types = {
        "json": json.loads,
        "yml": yaml.safe_load,
        "yaml": yaml.safe_load
    }
    parser = file_types.get(file_extension)

    if parser:
        return parser(file_data)

    else:
        raise Exception(
            'Invalid file type (only supports *.json and *.yaml/*.yml)'
        )
