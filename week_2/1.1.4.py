def complexArithmetics(a , b):
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b
    }


print(complexArithmetics(2+3j, 4+5j))