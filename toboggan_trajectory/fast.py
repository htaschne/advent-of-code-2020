
G = [line.rstrip() for line in open('0.in').readlines()]

# for i, line in enumerate(G):
#   for j, char in enumerate(line):
#     print(char, end='')
#   print()

ym, xm = len(G), len(G[0])

L = []

x = 0
y = 0
ret = 0
while y < ym:
  x = (x + 3) % xm
  y += 1

  if y >= ym or x >= xm:
    break

  if G[y][x] == '#':
    ret += 1

L.append(ret)


x = 0
y = 0
ret = 0
while y < ym:
  x = (x + 1) % xm
  y += 1

  if y >= ym or x >= xm:
    break

  if G[y][x] == '#':
    ret += 1

L.append(ret)

x = 0
y = 0
ret = 0
while y < ym:
  x = (x + 5) % xm
  y += 1

  if y >= ym or x >= xm:
    break

  if G[y][x] == '#':
    ret += 1

L.append(ret)

x = 0
y = 0
ret = 0
while y < ym:
  x = (x + 7) % xm
  y += 1

  if y >= ym or x >= xm:
    break

  if G[y][x] == '#':
    ret += 1

L.append(ret)

x = 0
y = 0
ret = 0
while y < ym:
  x = (x + 1) % xm
  y += 2

  if y >= ym or x >= xm:
    break

  if G[y][x] == '#':
    ret += 1

L.append(ret)

res = 1
for item in L:
  res *= item

print(res)
