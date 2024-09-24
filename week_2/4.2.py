def factorialCalculator(num):
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    
    print(factorial)


factorialCalculator(4)
factorialCalculator(5)
factorialCalculator(6)
factorialCalculator(8)
factorialCalculator(10)