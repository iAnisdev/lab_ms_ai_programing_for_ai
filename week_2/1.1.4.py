def complexArithmetics(a , b):
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b,
        'modulus':  abs(a+b) # To calculate the modulus of a complex number, you can use the built-in abs() function
    }


print(complexArithmetics(2+3j, 4+5j))