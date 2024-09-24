def bitwiseImplementation(a, b):
    return {
        'and': a & b,
        'or': a | b,
        'xor': a ^ b,
        'not': ~a,
        'left_shift': a << 2,
        'right_shift': a >> 2
    }

print(bitwiseImplementation(2, 3))
print(bitwiseImplementation(12, 8))
print(bitwiseImplementation(65, 32))