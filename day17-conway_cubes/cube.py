import sys

def boundaries(coord, cubes):
  return range(min([p[coord] for p in cubes])-1, max([p[coord] for p in cubes])+2)

def neighbors(x, y, z, w, cubes):
  nbrs = 0
  for dx in range(-1, 2): # -1, 0, 1
    for dy in range(-1, 2):
      for dz in range(-1, 2):
        for dw in range(-1, 2):
          if (dx, dy, dz, dw) != (0, 0, 0, 0) and (x+dx, y+dy, z+dz, w+dw) in cubes:
            nbrs += 1
  return nbrs

lines = [line.rstrip() for line in open(sys.argv[1]).readlines()]

cubes = set()
for r, line in enumerate(lines):
  for c, ch in enumerate(line):
    if ch == '#':
      cubes.add((r, c, 0, 0))

for cycle in range(6):

  # print(cycle)
  next_cubes = set()

  # not so infinite grid
  for x in boundaries(0, cubes):
    for y in boundaries(1, cubes):
      for z in boundaries(2, cubes):
        # part I change w range
        # for w in [0]:
        for w in boundaries(3, cubes):
          nbrs = neighbors(x, y, z, w, cubes)

          if (x, y, z, w) not in cubes and nbrs == 3:
            next_cubes.add((x, y, z, w))

          if (x, y, z, w) in cubes and (nbrs == 2 or nbrs == 3):
            next_cubes.add((x, y, z, w))

  cubes = next_cubes

print(len(cubes))
