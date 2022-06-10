from gendiff.formatters.stylish import format_to_stylish
from gendiff.formatters.plain import format_to_plain


def get_formatter(diff, form):
    forms = {
        'stylish': format_to_stylish,
        'plain': format_to_plain
    }
    return forms.get(form)(diff)
