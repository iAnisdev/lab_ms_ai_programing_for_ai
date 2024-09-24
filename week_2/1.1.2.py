a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

def checkGreaterNum(a , b):
    if a > b:
        print(f"The first number {a} is greater than the second number {b}.")
    elif a < b:
        print(f"The second number {b} is greater than the first number {a}.")
    else:
        print(f"The first number {a} is equal to the second number {b}.")

checkGreaterNum(a , b)