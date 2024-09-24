def generate_fibonacci(limit):
    series = [0 , 1]
    while len(series) < limit:
        series.append(series[len(series) - 1] + series[len(series) - 2])
    
    return series

upto = int(input("Enter a number for fibonacci series count: "))
print(generate_fibonacci(upto))