def fibonacci_sequence():
    a , b = 0 , 1
    while True:
        yield a
        a , b = b , a + b


fib = fibonacci_sequence()

upto = int(input("Enter a number for fibonacci series count: "))

for _ in range(upto):
    print(next(fib))
