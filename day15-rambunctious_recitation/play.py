import sys

from collections import defaultdict

nums = list(map(int, open(sys.argv[1]).readline().split(',')))

last = 0
lasts = defaultdict(list)
for i in range(30000000):
  if i < len(nums):
    last = nums[i]

  elif len(lasts[last]) == 1:
    last = 0

  elif len(lasts[last]) > 1:
    last = lasts[last][-1] - lasts[last][-2]

  lasts[last].append(i+1)

  if i == 2019:
    print(last)

print(last)
