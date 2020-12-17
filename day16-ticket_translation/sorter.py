
from collections import defaultdict

RR = defaultdict(list)

for line in open('out').readlines():
  line = line.rstrip().split(' ')
  space, rule = line[1], line[8]
  space = int(space)
  rule = int(rule)
  RR[space].append(rule)

# for k in RR:
for k in range(20):
  ret = []
  # print(k, sorted(RR[k]))
  for i in range(20):
    if i not in RR[k]:
      ret.append(i)
  ret = sorted(ret)
  print(k, ret)
