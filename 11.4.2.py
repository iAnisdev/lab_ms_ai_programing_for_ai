import math
def search_binary(arr , target):
    left_starting = 0
    right_starting = len(arr) 
    middle = math.floor(( left_starting + right_starting) / 2)
    if target > arr[right_starting - 1]:
       return FileNotFoundError("Item out of range")
    if target == arr[middle]:
        return target
    elif target > arr[middle]:
        search_binary(arr[middle:], target)
    elif target < arr[middle]:
        print(target , arr[middle])
        search_binary(arr[:middle], target)




print(search_binary([1,2,3,4,5,6,7,8] , 5))
print(search_binary([1,2,3,4,5,6,7,8] , 9))