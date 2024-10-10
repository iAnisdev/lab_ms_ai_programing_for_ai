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


print(sumKeys({1: 10, 2: 20, 3: 30}, {1: 10, 2: 20, 3: 30}))
print(sumKeys({1: 10, 2: 20, 3: 30}, {4: 10, 5: 20, 6: 30}))
print(sumKeys({1: 10, 2: 20, 3: 30}, {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}))