from functools import reduce

even_nums = [e for e in range(100, 1001, 2)]
prod = reduce(lambda p, e: p * e, even_nums, 1)
print(prod)