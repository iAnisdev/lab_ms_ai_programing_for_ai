def doOperation(a, b):
    setA = set(a)
    setB = set(b) 

    intersection = setA & setB
    symmetric_difference = setA ^ setB
    difference = setA - setB

    print({
        'intersection': intersection,
        'symmetric_difference': symmetric_difference,
        'difference': difference
    })


strA = input("Enter a string: ")
strB = input("Enter another string: ")

doOperation(strA, strB)