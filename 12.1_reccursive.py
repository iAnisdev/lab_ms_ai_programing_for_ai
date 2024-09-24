

def generate_fibonacci(limit , fib_sequence = [0 , 1]):
   fib_sequence.append(fib_sequence[len(fib_sequence) - 1] + fib_sequence[len(fib_sequence) - 2])
   if len(fib_sequence) < limit:
     return generate_fibonacci(limit , fib_sequence)
   else:
      return fib_sequence


upto = int(input("Enter a number for fibonacci series count: "))

series = generate_fibonacci(upto)
print(series)