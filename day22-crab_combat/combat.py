
import sys

from collections import deque

p1, p2 = open(sys.argv[1]).read().strip().split("\n\n")

p1 = deque(list(map(int, [x.rstrip() for x in p1.split("\n")][1:])))
p2 = deque(list(map(int, [x.rstrip() for x in p2.split("\n")][1:])))

def simulate(p1, p2):

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


ret = simulate(p1, p2)
acc = 0
for i in range(len(ret)):
  acc += ret[i] * (len(ret) - i)
print(acc)
