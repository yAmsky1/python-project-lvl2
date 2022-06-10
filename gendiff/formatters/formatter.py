from gendiff.formatters.stylish import format_to_stylish
from gendiff.formatters.plain import format_to_plain
from gendiff.formatters.json import format_to_json


def get_formatter(diff, form):
    forms = {
        'stylish': format_to_stylish,
        'plain': format_to_plain,
        'json': format_to_json
    }
    return forms.get(form)(diff)
