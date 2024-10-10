def mergeAndSort(list1, list2):
    merged = list1 + list2
    merged.sort()
    unique = []

    for i in merged:
        if i not in unique:
            unique.append(i)

    return unique


list1 = [1, 2, 8,  3, 4, 5]
list2 = [6, 3 , 11 , 7, 8 ,4, 5 ]

print("Merged and sorted list:", mergeAndSort(list1, list2))

list3 = [22, 18, 12, 7, 6, 11, 9]
list4 = [3, 5, 8, 22, 18, 12, 7, 6, 11, 9]

print("Merged and sorted list:", mergeAndSort(list3, list4))