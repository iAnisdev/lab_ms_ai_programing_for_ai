def medianFinder(list):
    list.sort()
    length = len(list)
    if len(list) %2 == 0:
        middle = length // 2
        sum_of_middle = list[middle] + list[middle - 1]
        return sum_of_middle / 2
    else:
        return list[length // 2]
    

# Test Cases
print(medianFinder([1, 2, 3, 4, 5])) # 3
print(medianFinder([1, 2, 3, 4, 5, 6])) # 3.5
print(medianFinder([1, 2, 3, 4, 5, 6, 7])) # 4
print(medianFinder([1, 2, 3, 4, 5, 6, 7, 8])) # 4.5
print(medianFinder([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 5