from gendiff.tags import ADDED, REMOVED, CHANGED, NESTED


ADDED_PROP = 'Property {0} was added with value: {1}'
REMOVED_PROP = 'Property {0} was removed'
CHANGED_PROP = 'Property {0} was updated. From {1} to {2}'


# Линтер жалуется "C901 'format_to_plain' is too complex (8)".
# Пока не придумал как упростить :(
def format_to_plain(diff, path=None):  # noqa: C901
    if path is None:
        path = []
    result = []
    for key, value in sorted(diff.items()):
        path.append(key)
        if isinstance(value, list):
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
                        edit_value(rest_values[0]),
                        edit_value(rest_values[1])
                    )
                )
            if tag == ADDED:
                result.append(
                    ADDED_PROP.format(
                        '.'.join(path),
                        edit_value(rest_values[0])
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


def edit_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    return value
