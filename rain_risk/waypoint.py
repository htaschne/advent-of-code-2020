import sys

def rot90(direction, p):
  return (-p[1], p[0]) if direction == 'L' else (p[1], -p[0])

def rotate(direction, amount, x, y):
  times = amount // 90 # garanteed to be integer
  for time in range(times):
    x, y = rot90(direction, (x, y))
  return x, y

def main():
  x, y = 0, 0
  wx, wy = 10, 1
  for l in open(sys.argv[1]).readlines():
    direction, amount = l[0], int(l[1:])
    if direction == 'N':
      wy += amount
    elif direction == 'S':
      wy -= amount
    elif direction == 'E':
      wx += amount
    elif direction == 'W':
      wx -= amount
    elif direction == 'L' or direction == 'R':
      wx, wy = rotate(direction, amount, wx, wy)
    elif direction == 'F':
      x += amount * wx
      y += amount * wy

  print(x, y)
  print(abs(x) + abs(y))

main()
