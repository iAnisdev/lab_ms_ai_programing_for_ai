str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

set1 = set(str1)
set2 = set(str2)

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))