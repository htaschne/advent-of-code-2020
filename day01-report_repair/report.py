import sys

entries = [int(x.rstrip()) for x in open(sys.argv[1]).readlines()]

def fix_by_two():
  global entries
  for i in range(len(entries)):
    r = entries[i]
    for j in range(i+1, len(entries)):
      l = entries[j]
      if l + r == 2020:
        print(l*r)
        return

def fix_by_three():
  global entries
  for i in range(len(entries)):
    lo = entries[i]
    for j in range(i+1, len(entries)):
      mi = entries[j]
      for k in range(j+1, len(entries)):
        hi = entries[k]

        if lo + mi + hi == 2020:
          print(lo * mi * hi)
          return

fix_by_two()
fix_by_three()
