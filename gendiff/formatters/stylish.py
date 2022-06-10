from gendiff.tags import ADDED, REMOVED, UNCHANGED, CHANGED, NESTED

TAGS = {
    ADDED: '+',
    REMOVED: '-',
    UNCHANGED: ' ',
    NESTED: ' '
}
REPLACER = '   '
SPACES_COUNT = 1


def format_to_stylish(diff, depth=0):
    indent = depth * REPLACER * SPACES_COUNT
    res = []
    for key, value in sorted(diff.items()):
        if isinstance(value, list):
            tag, *rest_values = value
            if tag == CHANGED:
                res.append(gen_string(REMOVED, key, rest_values[0], depth + 1))
                res.append(gen_string(ADDED, key, rest_values[1], depth + 1))
                continue
            res.append(gen_string(tag, key, rest_values[0], depth + 1))
            continue
        res.append(gen_string(UNCHANGED, key, value, depth + 1))
    return '{\n' + '\n'.join(res) + '\n' + indent + '}'


def gen_string(tag, key, value, depth):
    indent = depth * REPLACER * SPACES_COUNT
    if isinstance(value, dict):
        result = format_to_stylish(value, depth)
        return f"{indent}{TAGS.get(tag)} {key}: {result}"
    return f"{indent}{TAGS.get(tag)} {key}: {edit_value(value)}"


def edit_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    if value is None:
        return 'null'
    return value
