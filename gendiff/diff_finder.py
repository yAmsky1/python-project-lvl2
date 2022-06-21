ADDED = 'ADDED'
REMOVED = 'REMOVED'
UNCHANGED = 'UNCHANGED'
NESTED = 'NESTED'
CHANGED = 'CHANGED'


def check_diff(data1, data2):
    diff = []
    added_keys = list(data2.keys() - data1.keys())
    removed_keys = list(data1.keys() - data2.keys())
    common_keys = list(data1.keys() & data2.keys())

    for key in added_keys:
        diff.append(
            generate_branch(
                key,
                ADDED,
                new_value=data2.get(key)
            )
        )

    for key in removed_keys:
        diff.append(
            generate_branch(
                key,
                REMOVED,
                old_value=data1.get(key)
            )
        )

    for key in common_keys:
        old_value = data1.get(key)
        new_value = data2.get(key)

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            diff.append(
                generate_branch(
                    key,
                    NESTED,
                    nested=check_diff(old_value, new_value)
                )
            )

        elif old_value == new_value:
            diff.append(
                generate_branch(
                    key,
                    UNCHANGED,
                    old_value=old_value
                )
            )

        else:
            diff.append(
                generate_branch(
                    key,
                    CHANGED,
                    old_value=old_value,
                    new_value=new_value
                )
            )
    diff.sort(key=lambda a: a['key'])
    return diff


def generate_branch(key, tag, old_value=None, new_value=None, nested=None):
    branch = {
        'key': key,
        'tag': tag,
        'old_value': old_value,
        'new_value': new_value,
        'nested': nested
    }

    return branch
