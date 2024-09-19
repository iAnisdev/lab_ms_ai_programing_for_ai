prime_number = []
for a in range(0, 101):
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                break
            else:
                prime_number.append(a)
            break

print(prime_number)