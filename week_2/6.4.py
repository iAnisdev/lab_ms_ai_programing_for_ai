def listFlatten(nestedList):
    flatList = []
    for i in nestedList:
        if type(i) == list:
            flatList.extend(listFlatten(i))
        else:
            flatList.append(i)
    return flatList


nestedList = [1, 2, [3, 4, [5, 6], 7], 8, [9, 10]]
print("Nested list:", nestedList)

print("Flattened list:", listFlatten(nestedList))

nestedList = [1, [5, 6], 7], 8, [9, 10 , [2 , 7 , [8 , 9]]]
print("Nested list:", nestedList)

print("Flattened list:", listFlatten(nestedList))