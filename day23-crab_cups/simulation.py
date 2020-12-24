import sys

from typing import List
from collections import deque

def rotate_left(cups, x):
  for _ in range(x):
    v = cups.pop(0)
    cups.append(v)
  return cups

def rotate_right(cups, x):
  s = []
  for _ in range(x):
    s.append(cups.pop())
  ret = []
  while len(s) > 0:
    ret.append(s.pop())
  for k in cups:
    ret.append(k)
  return ret

def rotate(cups, pos, k):
  # print("pos", pos,"k", k)
  val = cups[pos]
  x = pos - k
  # print(x)
  if x < 0:
    # print("rotate right by: %d units" % x)
    cups = rotate_right(cups, abs(x))
  else:
    cups = rotate_left(cups, x)

  # print(cups)
  return cups, cups.index(val)


def show(cups, pos):
  print("cups: ", end="")
  for i, x in enumerate(cups):
    if i == pos:
      print("(%d) " % x, end="")
    else:
      print("%d " % x, end="")
  print()

def split(cups, pos):
  #print("POS POS POS", pos, len(cups))
  a, b = [], []
  cups = deque(cups)

  if pos == 9:
    b = [cups.popleft() for _ in range(3)]
    a = [cups.popleft() for _ in range(len(cups))]
    return a, b

  if pos == 0:
    a.append(cups.popleft())
    for _ in range(3):
      b.append(cups.popleft())
    while len(cups) > 0:
      a.append(cups.popleft())
    return a, b
  
  p = 0
  while p != pos:
    # print(p, a)
    a.append(cups.popleft())
    p += 1

  if len(cups) == 0:
    return a, b

  n = 0
  for _ in range(3):
    if len(cups) == 0:
      break
    b.append(cups.popleft())
    n += 1

  while len(b) != 3:
    b.append(a.pop(0))

  while len(cups) > 0:
    a.append(cups.popleft())

  return a, b


def step(cups: List[int], pos: int) -> (List[int], int):
  # show(cups, pos)
  small, hold = split(cups, pos+1)
  if len(hold) < 3:
    print("not holding enough values")
    print(small, hold)

  # print("pick up:", ', '.join([str(x) for x in hold]))
  aim = cups[pos] - 1
  while aim not in small and aim > 0:
    aim = aim - 1

  if aim == 0:
    aim = max(small)

  new_pos = small.index(aim)

  # print("destination:", small[new_pos])

  small = deque(small)
  l = [small.popleft() for _ in range(new_pos+1)]
  for x in hold:
    l.append(x)
  for x in small:
    l.append(x)

  ret = l, (l.index(cups[pos])+1) % len(cups)
  return ret



cups = list(map(int, list(open(sys.argv[1]).readline().rstrip())))

# step([3, 2, 8, 9, 1, 5, 4, 6, 7], 2)

pos = 0
for k in range(100):
  # print("-- move %d --" % (k + 1))
  cups, pos = step(cups, pos)
  if pos != (k+1) % len(cups):
    # print("need rotate", cups, pos, (k+1)%len(cups))
    cups, pos = rotate(cups, pos, (k+1)%len(cups))
    # print(cups)
  # print()
print("-- final --")
show(cups, pos)
print(''.join(str(x) for x in cups))


