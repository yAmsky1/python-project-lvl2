from gendiff.formatters.stylish import format_to_stylish


def get_formatter(diff, form):
    forms = {
        'stylish': format_to_stylish
    }
    return forms.get(form)(diff)
