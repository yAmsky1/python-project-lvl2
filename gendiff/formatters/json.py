import json


def format_to_json(diff):
    return json.dumps(diff, sort_keys=True, indent=2)
