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
    # print(curr)
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
mask = ''
for line in open(sys.argv[1]).readlines():
  if 'mask' in line:
    mask = line.rstrip().split(' = ')[1]
  else:
    pos, tail = line = line[4:].split(']')
    pos = int(pos)
    value = int(tail.strip().split('= ')[1])
    pos = fix(list(bin(int(pos)))[2:])
    # print(''.join(pos), value)
    Q = []
    find(pos, mask, 0, '')

    for addr in Q:
      addr = int(''.join(addr), 2)
      mem[addr] = value

s = 0
for k in mem:
  s += mem[k]
print(s)
