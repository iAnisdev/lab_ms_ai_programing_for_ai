file = open('11.3.1_the_sieve_of_eratosthenes_algorithm.py', 'r')

content = file.read()

word_counter = {}

for word in content.split():
    if word.lower() not in ["and", "the"]:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

print(word_counter)