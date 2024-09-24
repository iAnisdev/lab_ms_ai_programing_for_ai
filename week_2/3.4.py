import re
def passwordValidator(password):
    validationPattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if re.match(validationPattern, password):
        return True
    else:
        return False
    

passwords = ['NCI20204', 'Password' , 'NCI2024*' , 'Nci2024*']

for password in passwords:
    print(passwordValidator(password))