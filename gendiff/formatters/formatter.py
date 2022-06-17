from gendiff.formatters.stylish import format_to_stylish
from gendiff.formatters.plain import format_to_plain
from gendiff.formatters.json import format_to_json


STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
ERROR = ' Invalid format choice: {0} (choose from "stylish", "plain", "json") '


def get_formatter(diff, format_style):
    format_values = {
        STYLISH: format_to_stylish,
        PLAIN: format_to_plain,
        JSON: format_to_json
    }
    formatter = format_values.get(format_style)
    return formatter(diff) if formatter else ERROR.format(format_style)
