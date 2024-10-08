def findPrimes(limit):
    primes = []

    for number in range(2, limit + 1):

        for i in range(2, number):
            if number % i == 0:
                break
        else:
            primes.append(number)

    return primes


print(findPrimes(10))

print(findPrimes(50))

print(findPrimes(100))
