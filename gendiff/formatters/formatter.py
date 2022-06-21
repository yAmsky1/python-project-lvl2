from gendiff.formatters.stylish import format_to_stylish
from gendiff.formatters.plain import format_to_plain
from gendiff.formatters.json import format_to_json


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def get_formatter(diff, format_style):
    format_values = {
        STYLISH: format_to_stylish,
        PLAIN: format_to_plain,
        JSON: format_to_json
    }
    formatter = format_values.get(format_style)
    if formatter:
        return formatter(diff)
    else:
        raise Exception(
            'Invalid format choice(choose from "stylish", "plain", "json")'
        )
