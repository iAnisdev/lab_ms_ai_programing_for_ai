import re
email = str(input("Enter your email: "))

email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
if re.match(email_pattern, email):
    print(f"{email} is a valid email address")
else:
    print(f"{email} is not a valid email address")


