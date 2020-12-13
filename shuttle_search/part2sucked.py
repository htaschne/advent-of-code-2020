import sys

from functools import reduce

# https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


lines = [line.rstrip() for line in open(sys.argv[1])]
buses = [[int(t), n] for n, t in enumerate(lines[1].split(",")) if t != "x"]

n = [x[0] for x in buses]
a = [x[0] - x[1] % x[0] for x in buses]

print(chinese_remainder(n, a))
