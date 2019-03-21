import math
factors = list(range(1,101))

def reduce_base10(factors):
    for _ in range(2):
        factors = (f // (10 if not (f % 10) else 1) for f in factors)
    return factors

prod = lambda x, y: x * y


print(list(reduce_base10(factors)))
print(reduce(prod, reduce_base10(factors)))
print(math.log(reduce(prod, reduce_base10(factors)), 2) / 64)

print()
