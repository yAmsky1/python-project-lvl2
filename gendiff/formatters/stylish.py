from gendiff.diff_finder import ADDED, REMOVED, UNCHANGED, CHANGED, NESTED


REPLACER = ' '
SPACES_COUNT = 2
TAGS = {
    ADDED: '+',
    REMOVED: '-',
    UNCHANGED: ' ',
    NESTED: ' ',
    REPLACER: ' '
}


def format_to_stylish(diff, depth=0):  # noqa: C901
    indent = depth * REPLACER * SPACES_COUNT
    result = []
    for key, value in sorted(diff.items()):

        if not isinstance(value, dict):
            result.append(gen_string(REPLACER, key, value, depth + 1))

        else:
            tag = value.get('tag')

            if tag == CHANGED:
                old_value = value.get('old_value')
                new_value = value.get('new_value')
                result.append(gen_string(REMOVED, key, old_value, depth + 1))
                result.append(gen_string(ADDED, key, new_value, depth + 1))

            elif tag == UNCHANGED:
                value = value.get('old_value')
                result.append(gen_string(UNCHANGED, key, value, depth + 1))

            elif tag == ADDED:
                value = value.get('new_value')
                result.append(gen_string(ADDED, key, value, depth + 1))

            elif tag == REMOVED:
                value = value.get('old_value')
                result.append(gen_string(REMOVED, key, value, depth + 1))

            elif tag == NESTED:
                value = value.get('nested')
                result.append(gen_string(NESTED, key, value, depth + 1))

            else:
                result.append(gen_string(REPLACER, key, value, depth + 1))

    return '{\n' + '\n'.join(result) + '\n' + indent + '}'


def gen_string(tag, key, value, depth):
    indent = depth * REPLACER * SPACES_COUNT

    if isinstance(value, dict):
        result = format_to_stylish(value, depth + 1)
        return f"{indent}{TAGS.get(tag)} {key}: {result}"

    return f"{indent}{TAGS.get(tag)} {key}: {format_value(value)}"


def format_value(value):

    if isinstance(value, bool):
        value = str(value).lower()

    if value is None:
        return 'null'

    return value
