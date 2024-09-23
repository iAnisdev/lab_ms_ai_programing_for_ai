import math

def search_binary(arr , target):
    left = 0
    right = len(arr) -1

    while left <=  right:
        mid = math.floor(( left + right) / 2)

        if target == arr[mid]:
            return arr[mid]
        
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

        
    

print(search_binary([1,2,3,4,5,6,7,8] , 5))
print(search_binary([1,2,3,4,5,6,7,8] , 9))