
import sys

''' N
  W   E
    S
'''

def rotate(dd, amount, face):
  d = ['N', 'W', 'S', 'E']
  if amount == 90:
    for i in range(4):
      if d[i] == face:
        x = 1 if dd == 'L' else -1
        ret = d[(i+x)%4]
        return ret
  elif amount == 180:
    for i in range(4):
      if d[i] == face:
        x = 2 if dd == 'L' else -2
        ret = d[(i+x)%4]
        return ret
  elif amount == 270:
    for i in range(4):
      if d[i] == face:
        x = 3 if dd == 'L' else -3
        ret = d[(i+x)%4]
        return ret
  else:
    print('got unmatched amount: %d' % amout)

def main():
  x, y = 0, 0
  face = 'E'
  for l in open(sys.argv[1]).readlines():
    direction, amount = l[0], int(l[1:])
    if direction == 'N':
      y += amount
    elif direction == 'S':
      y -= amount
    elif direction == 'E':
      x += amount
    elif direction == 'W':
      x -= amount
    elif direction == 'L' or direction == 'R':
      face = rotate(direction, amount, face)
    elif direction == 'F':
      xx = x
      yy = y
      if face == 'N':
        y += amount
      elif face == 'S':
        y -= amount
      elif face == 'E':
        x += amount
      elif face == 'W':
        x -= amount
    else:
      print('got unmatched direction %s' % direction)
  print(x, y)
  print(abs(x) + abs(y))

main()
