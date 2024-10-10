def findLargeValueInDict(d):
    values = list(d.values())
    max_value = max(values)
    max_value_index = values.index(max_value)
    keys = list(d.keys())
    max_key = keys[max_value_index]
    return max_key


print(findLargeValueInDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
print(findLargeValueInDict({'a': 1, 'b': 2, 'c': 133, 'd': 4, 'e': 10}))
print(findLargeValueInDict({'a': 1, 'b': 2, 'c': 3, 'd': 14, 'e': 5}))