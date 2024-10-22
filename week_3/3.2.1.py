def ask_user_for_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def calculate_sum():
    print("Enter two integers to calculate their sum.")
    a = ask_user_for_number("Enter the first number: ")
    b = ask_user_for_number("Enter the second number: ")
    

    print(f"The sum of {a} and {b} is {a + b}.")

calculate_sum()