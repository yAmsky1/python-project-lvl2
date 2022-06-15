ADDED = 'ADDED'
REMOVED = 'REMOVED'
UNCHANGED = 'UNCHANGED'
NESTED = 'NESTED'
CHANGED = 'CHANGED'


def check_diff(data1, data2):
    diff = {}
    added_keys = list(data2.keys() - data1.keys())
    removed_keys = list(data1.keys() - data2.keys())
    common_keys = list(data1.keys() & data2.keys())
    for key in added_keys:
        diff[key] = [ADDED, data2.get(key)]
    for key in removed_keys:
        diff[key] = [REMOVED, data1.get(key)]
    for key in common_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = [NESTED, check_diff(value1, value2)]
        elif value1 == value2:
            diff[key] = [UNCHANGED, value1]
        else:
            diff[key] = [CHANGED, value1, value2]
    return diff
