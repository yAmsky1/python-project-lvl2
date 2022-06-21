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
TEMPLATE_HEAD = "{indent}{tag} {key}: {{"
TEMPLATE_TAIL = "  {indent}}}"
TEMPLATE_VALUE = "{indent}{tag} {key}: {value}"


def format_to_stylish(diff):
    return '\n'.join(prepare_for_stylish(diff))


def prepare_for_stylish(diff, depth=0):  # noqa: C901

    if depth == 0:
        result = ["{"]

    else:
        result = []

    for node in diff:
        tag = node.get('tag')
        key = node.get('key')

        if tag == CHANGED:
            old_value = node.get('old_value')
            new_value = node.get('new_value')
            result.append(generate_string(REMOVED, key, old_value, depth + 1))
            result.append(generate_string(ADDED, key, new_value, depth + 1))

        elif tag == UNCHANGED:
            value = node.get('old_value')
            result.append(generate_string(UNCHANGED, key, value, depth + 1))

        elif tag == ADDED:
            value = node.get('new_value')
            result.append(generate_string(ADDED, key, value, depth + 1))

        elif tag == REMOVED:
            value = node.get('old_value')
            result.append(generate_string(REMOVED, key, value, depth + 1))

        elif tag == NESTED:
            value = node.get('nested')
            result.append(generate_string(NESTED, key, value, depth + 1))

    if depth == 0:
        result.append("}")

    return result


def generate_string(tag, key, node, depth):
    indent = (depth * REPLACER * SPACES_COUNT)
    tag = TAGS.get(tag)

    if isinstance(node, dict):
        string = [TEMPLATE_HEAD.format(indent=indent, tag=tag, key=key)]

        for key in node:
            string.append(generate_string(REPLACER, key,
                                          node[key], depth + 2))
        string.append(TEMPLATE_TAIL.format(indent=indent))
        return '\n'.join(string)

    elif isinstance(node, list):
        string = [TEMPLATE_HEAD.format(indent=indent, tag=tag, key=key)]
        string.extend(prepare_for_stylish(node, depth + 1))
        string.append(TEMPLATE_TAIL.format(indent=indent))
        return '\n'.join(string)

    else:
        return TEMPLATE_VALUE.format(indent=indent, tag=tag,
                                     key=key, value=format_value(node))


def format_value(value):

    if isinstance(value, bool):
        value = str(value).lower()

    if value is None:
        return 'null'
    return value
