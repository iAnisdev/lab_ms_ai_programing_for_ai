# The sieve of eraosthenes algorithm is a simple and ancient algorithm used to find all prime numbers up to a given limit.
# It does so by iteratively marking the multiples of each prime number starting from 2, up to the square root of the limit.
# The algorithm consists of repeating the following over and over:
# 1. Find the next number p not yet crossed out.
# 2. Cross out all multiples of p which are not already crossed out.
# 3. The numbers that are not crossed out are the primes.
# Time complexity: O(n log log n) and space complexity: O(n) because the algorithm uses a list of n elements.


def sieve_of_eratosthenes (limit):
    # Create a boolean array "prime[0..n]" and initialize all elements as True.
    prime = [True] * (limit + 1)
    # Set the 0 and 1 as False because they are not prime numbers.
    starting_number = 2

    while(starting_number * starting_number <= limit):
        # If prime[starting_number] is not changed, then it is a prime.
        if prime[starting_number] == True:
            # Update all multiples of starting_number with step of starting_number.
            for i in range(starting_number * starting_number, limit + 1 , starting_number):
                prime[i] = False

        # Move to the next number.
        starting_number += 1

        # clean up the list of prime numbers and only print the prime numbers which are True.
    primes_found = [number for number in range(2 , limit + 1) if prime[number] == True]
    return primes_found


print(sieve_of_eratosthenes(10))
print(sieve_of_eratosthenes(50))
print(sieve_of_eratosthenes(100))