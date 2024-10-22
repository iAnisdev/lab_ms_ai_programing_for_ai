def check_index(lst, index):
    try:
        if lst[index]:
            return lst[index]
        else:
            raise IndexError
    except IndexError:
        print(f"Error: Index out of range.")


lst = [1, 2, 3, 4, 5]

print(check_index(lst, 0))
print(check_index(lst, 2))
print(check_index(lst, 5))
