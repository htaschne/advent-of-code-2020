import sys

from math import ceil, floor
from collections import deque

tickets = [deque(line.rstrip()) for line in open(sys.argv[1]).readlines()]

seats = []
highest = 0
for ticket in tickets:
  lo, hi = 0, 127
  for _ in range(7):
    letter = ticket.popleft()
    if letter == "F":
      hi = floor((hi+lo)/2)
    else:
      lo = ceil((lo+hi)/2)

  row = lo

  lo, hi = 0, 7
  for _ in range(3):
    letter = ticket.popleft()
    if letter == "R":
      lo = ceil((lo+hi)/2)
    else:
      hi = floor((lo+hi)/2)

  col = hi

  seat_id = row * 8 + col
  highest = max(seat_id, highest)
  seats.append(seat_id)

print(highest)

seats = sorted(seats)
for i in range(len(seats)-1):
  if seats[i]+1 != seats[i+1]:
    print(seats[i] + 1)
    break
