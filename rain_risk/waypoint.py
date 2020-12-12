import sys

def rot(dd, x, y):
  if dd == 'L':
    return -y, x
  else:
    return y, -x

def rotate(dd, amount, x, y):
  if amount == 90:
    return rot(dd, x, y)
  elif amount == 180:
    x, y = rot(dd, x, y)
    return rot(dd, x, y)
  elif amount == 270:
    x, y = rot(dd, x, y)
    x, y = rot(dd, x, y)
    return rot(dd, x, y)

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
