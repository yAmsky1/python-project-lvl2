from gendiff.diff_finder import ADDED, REMOVED, CHANGED, NESTED


ADDED_PROP = "Property '{0}' was added with value: {1}"
REMOVED_PROP = "Property '{0}' was removed"
CHANGED_PROP = "Property '{0}' was updated. From {1} to {2}"


def format_to_plain(diff):
    return '\n'.join(prepare_for_plain(diff))


def prepare_for_plain(diff, path=None):  # noqa: C901

    if path is None:
        path = []
    result = []

    for node in diff:
        key = node.get('key')
        tag = node.get('tag')
        path.append(key)

        if tag == NESTED:
            value = node.get('nested')
            result.extend(prepare_for_plain(value, path))

        if tag == CHANGED:
            old_value = node.get('old_value')
            new_value = node.get('new_value')
            result.append(
                CHANGED_PROP.format(
                    '.'.join(path),
                    format_value(old_value),
                    format_value(new_value)
                )
            )

        if tag == ADDED:
            value = node.get('new_value')
            result.append(
                ADDED_PROP.format(
                    '.'.join(path),
                    format_value(value)
                )
            )

        if tag == REMOVED:
            result.append(
                REMOVED_PROP.format(
                    '.'.join(path)
                )
            )

        path.pop()
    return sorted(result)


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
