def generate_fibonacci(limit):
    series = [0 , 1]
    while len(series) < limit:
        series.append(series[len(series) - 1] + series[len(series) - 2])
    
    return series


print(generate_fibonacci(10))
print(generate_fibonacci(20))