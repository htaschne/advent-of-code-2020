import sys

k1, k2 = list(map(int, [x for x in open(sys.argv[1]).readlines()]))
# print(k1, k2)
# k1, k2 = 5764801, 17807724

def transform(x, size):
  # know your math!
  return pow(x, size, 20201227)

  v = 1
  for _ in range(size):
    v = v * x
    v = v % 20201227
  return v

l1 = 0
while transform(7, l1) != k1:
  l1 += 1

l2 = 0
while transform(7, l2) != k2:
  l2 += 1

encryption = transform(k1, l2)
print(l1, l2, encryption)
