age = int(input("Enter your age: "))


if age < 12:
    print("Child")
elif age >= 12 and age <= 17:
    print("Teenager")
elif age >=18 and age <= 65:
    print("Adult")
else:
    print("Senior")