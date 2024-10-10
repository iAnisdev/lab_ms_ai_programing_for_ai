def sumKeys(d1, d2):
    sum = {}
    for key, value in d1.items():
        sum[key] = value

    for key, value in d2.items():
        if key in sum:
            sum[key] += value
        else:
            sum[key] = value
    return sum


print(sumKeys({'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'd': 6}))
print(sumKeys({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}))
print(sumKeys({'h': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'd': 6}))