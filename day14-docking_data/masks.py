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

Q = []
def find(pos, mask, i, curr):
  global Q
  if not i < 36:
    Q.append(curr)
    return

  if mask[i] == '1':
    find(pos, mask, i+1, curr+'1')
  elif mask[i] == 'X':
    find(pos, mask, i+1, curr+'1')
    find(pos, mask, i+1, curr+'0')
  elif mask[i] == '0':
    find(pos, mask, i+1, curr+pos[i])

mem = defaultdict(int)
for line in open(sys.argv[1]).readlines():
  if 'mask' in line:
    mask = line.rstrip().split(' = ')[1]
  else:
    address, raw_value = line[4:].split(']')
    address = int(address)
    value = int(raw_value.strip().split('= ')[1])
    address = fix(list(bin(int(address)))[2:])
    Q = []
    find(address, mask, 0, '')

    for addr in Q:
      addr = int(''.join(addr), 2)
      mem[addr] = value

print(sum([mem[k] for k in mem]))
