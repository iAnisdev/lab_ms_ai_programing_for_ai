complex_a = complex(input("Enter a complex number (e.g., 3+4j): "))
complex_b = complex(input("Enter another complex number (e.g., 3+4j): "))

print(complex_a , complex_b)

def magnitude_abs(complex_num):
    return abs(complex_num)


if magnitude_abs(complex_a) > magnitude_abs(complex_b):
    print(f"The magnitude of {complex_a} is greater than {complex_b}")
elif magnitude_abs(complex_a) < magnitude_abs(complex_b):
    print(f"The magnitude of {complex_b} is greater than {complex_a}")
else:
    print(f"The magnitude of {complex_a} and {complex_b} are equal")