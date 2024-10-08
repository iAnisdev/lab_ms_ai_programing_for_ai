def power(base , exponent):
   return base ** exponent

print(power(2, 3))


lambda_power = lambda base, exponent : base ** exponent


print(lambda_power(2, 3))

assert lambda_power(2, 3) == 8, "Should be 8"