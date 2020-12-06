import sys

from collections import defaultdict

def main():
  lines = [line.rstrip() for line in open(sys.argv[1]).readlines()]

  ret = 0
  rett = 0
  D = defaultdict(int)
  n = 0
  for line in lines:
    if len(line) == 0:
      rett += len(D.keys())
      for k in D.keys():
        if D[k] == n:
          ret += 1

      D = defaultdict(int)
      n = 0
      continue

    s = list(str(line))
    for char in s:
      D[char] += 1
    n += 1

  rett += len(D.keys())
  for k in D.keys():
    if D[k] == n:
      ret += 1

  print(rett, ret)

main()
