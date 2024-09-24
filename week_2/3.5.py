def gradChecker(marks):
    if marks > 100:
        print('You wish!')
    elif marks >= 90 and marks <=100:
        print('A')
    elif marks >= 80 and marks < 90:
        print('B')
    elif marks >= 70 and marks < 80:
        print('C')
    elif marks >= 60 and marks < 70:
        print('D')
    else:
        print('F')

    

gradChecker(120)
gradChecker(95)
gradChecker(84)
gradChecker(77)
gradChecker(66)
gradChecker(55)
gradChecker(52)
gradChecker(20)
