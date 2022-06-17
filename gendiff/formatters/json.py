import json
from gendiff.diff_finder import ADDED, REMOVED, UNCHANGED, CHANGED, NESTED


def format_to_json(diff):
    data = prepare_data_for_serialize(diff)
    return json.dumps(data, sort_keys=True, indent=2)


def prepare_data_for_serialize(diff):  # noqa: C901
    data = []

    for key, values in sorted(diff.items()):

        if not isinstance(diff, dict):
            data.append(
                {
                    'key': key,
                    'value': values
                }
            )

        else:
            tag = values.get('tag')

            if tag == ADDED:
                value = values.get('new_value')
                data.append(
                    {
                        'key': key,
                        'tag': tag,
                        'value': value
                    }
                )

            if tag == REMOVED:
                value = values.get('old_value')
                data.append(
                    {
                        'key': key,
                        'tag': tag,
                        'value': value
                    }
                )

            if tag == CHANGED:
                old_value = values.get('old_value')
                new_value = values.get('new_value')
                data.append(
                    {
                        'key': key,
                        'tag': tag,
                        'old_value': old_value,
                        'new_value': new_value
                    }
                )

            if tag == NESTED:
                value = prepare_data_for_serialize(values.get('nested'))
                data.append(
                    {
                        'key': key,
                        'tag': tag,
                        'value': value
                    }
                )

            if tag == UNCHANGED:
                value = values.get('old_value')
                data.append(
                    {
                        'key': key,
                        'tag': tag,
                        'value': value
                    }
                )

    return data
