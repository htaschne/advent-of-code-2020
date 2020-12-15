import sys

from collections import defaultdict

nums = list(map(int, open(sys.argv[1]).readline().split(',')))

counter = defaultdict(int)
lasts = defaultdict(list)
spoken = []
last = 0
for i in range(30000000):
  if i < len(nums):
    last = nums[i]

  elif counter[last] == 1:
    last = 0

  elif counter[last] > 1:
    # print(i, lasts[last], last)
    last = lasts[last][-1] - lasts[last][-2]

  spoken.append(last)
  lasts[last].append(i+1)
  counter[last] += 1

print(spoken[-1])
