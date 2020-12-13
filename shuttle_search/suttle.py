import sys


lines = [line.rstrip() for line in open(sys.argv[1]).readlines()]

station = int(lines[0])

diffs = []
buses = []
for bus in lines[1].split(','):
  if bus == 'x':
    continue
  bus = int(bus)
  t = bus
  while t < station:
    t += bus
  if t == station:
    print(bus)
    break
  else:
    diffs.append((t - station, t, bus))

mn, mnid, bus = diffs[0][0], diffs[0][1], diffs[0][2]

for i in range(1, len(diffs)):
  if diffs[i][0] < mn:
    mn = diffs[i][0]
    mnid = diffs[i][1]
    bus = diffs[i][2]

print(mn, mnid, bus, bus * mn)
