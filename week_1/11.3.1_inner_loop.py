def isPrime(num):
    if num < 2: return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
        return True


def findPrimes(limit):
    primes = []
    for i in range(2, limit):
        if isPrime(i):
            primes.append(i)
    return primes


print(findPrimes(100))