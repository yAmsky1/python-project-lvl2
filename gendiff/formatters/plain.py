from gendiff.diff_finder import ADDED, REMOVED, CHANGED, NESTED


ADDED_PROP = "Property '{0}' was added with value: {1}"
REMOVED_PROP = "Property '{0}' was removed"
CHANGED_PROP = "Property '{0}' was updated. From {1} to {2}"


def format_to_plain(diff, path=None):  # noqa: C901
    if path is None:
        path = []
    result = []
    for key, value in sorted(diff.items()):
        path.append(key)
        tag, *rest_values = value
        if tag == NESTED:
            result.append(
                format_to_plain(
                    rest_values[0],
                    path
                )
            )
        if tag == CHANGED:
            result.append(
                CHANGED_PROP.format(
                    '.'.join(path),
                    format_value(rest_values[0]),
                    format_value(rest_values[1])
                )
            )
        if tag == ADDED:
            result.append(
                ADDED_PROP.format(
                    '.'.join(path),
                    format_value(rest_values[0])
                )
            )
        if tag == REMOVED:
            result.append(
                REMOVED_PROP.format(
                    '.'.join(path)
                )
            )
        path.pop()
    return '\n'.join(sorted(result))


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return value
