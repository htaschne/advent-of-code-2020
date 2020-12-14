import sys

from collections import defaultdict

def fix(value):
  n = 36 - len(value)
  if n == 0:
    return value
  new_value = ['0' for _ in range(n)]
  for b in value:
    new_value.append(b)
  assert(len(new_value) == 36)
  return new_value

def result(value, mask):
  for i in range(36):
    if mask[i] == 'X':
      continue
    else:
      value[i] = mask[i]
  return int(''.join(value), 2)

mem = defaultdict(int)
for line in open(sys.argv[1]).readlines():
  if 'mask' in line:
    mask = line.rstrip().split(' = ')[1]
  else:
    pos, tail = line = line[4:].split(']')
    pos = int(pos)
    value = tail.strip().split('= ')[1]
    value = fix(list(bin(int(value)))[2:])
    mem[pos] = result(value, mask)

print(sum([mem[k] for k in mem]))
