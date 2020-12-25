import sys

from collections import deque

p1, p2 = open(sys.argv[1]).read().strip().split("\n\n")

p1 = deque(list(map(int, [x.rstrip() for x in p1.split("\n")][1:])))
p2 = deque(list(map(int, [x.rstrip() for x in p2.split("\n")][1:])))

def regular_combat(p1, p2):
  n = 1
  while True:
    # print("-- Round %d --" % (n+1))
    # print("Player 1's deck:", ", ".join([str(x) for x in p1]))
    # print("Player 2's deck:", ", ".join([str(x) for x in p2]))

    if len(p1) == 0:
      return p2
    if len(p2) == 0:
      return p1

    a, b = p1.popleft(), p2.popleft()
    # print("Player 1 plays:", a)
    # print("Player 2 plays:", b)

    if a > b:
      # print("Player 1 wins the round!")
      p1.append(a)
      p1.append(b)

    elif b > a:
      # print("Player 2 wins the round!")
      p2.append(b)
      p2.append(a)
    
    # print()
    n += 1


ret = regular_combat(p1.copy(), p2.copy())
acc = 0
for i in range(len(ret)):
  acc += ret[i] * (len(ret) - i)
print(acc)


def recursive_combat(deck1, deck2):
  rounds = [] # this should really be a set but whatever

  while len(deck1) != 0 and len(deck2) != 0:
    if (deck1, deck2) in rounds:
      return True

    rounds.append((deck1.copy(), deck2.copy()))

    c1 = deck1.pop(0)
    c2 = deck2.pop(0)

    # determine winner with a sub game
    if len(deck1) >= c1 and len(deck2) >= c2:
      winner = recursive_combat(deck1.copy()[:c1], deck2.copy()[:c2])

      if winner:
          deck1.append(c1)
          deck1.append(c2)
      else:
          deck2.append(c2)
          deck2.append(c1)

    # determine winner by card value
    else:
      if c1 > c2:
          deck1.append(c1)
          deck1.append(c2)
      elif c2 > c1:
          deck2.append(c2)
          deck2.append(c1)

  return len(deck1) != 0

d1 = [x for x in p1]
d2 = [x for x in p2]
ret = recursive_combat(d1, d2)
dd = d1 if ret else d2
acc = 0
for i in range(len(dd)):
  acc += dd[i] * (len(dd) - i)
print(acc)
