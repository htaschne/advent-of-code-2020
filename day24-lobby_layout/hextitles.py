import sys

# https://www.redblobgames.com/grids/hexagons/

titles = [line.strip() for line in open(sys.argv[1]).readlines()]

blacks = set()
for t in titles:
  x, y, z = 0, 0, 0
  i = 0
  while t:
    if t.startswith("e"):
      x += 1
      y -= 1
      t = t[1:]
    elif t.startswith("se"):
      y -= 1
      z += 1
      t = t[2:]
    elif t.startswith("sw"):
      x -= 1
      z += 1
      t = t[2:]
    elif t.startswith("w"):
      x -= 1
      y += 1
      t = t[1:]
    elif t.startswith("nw"):
      y += 1
      z -= 1
      t = t[2:]
    elif t.startswith("ne"):
      x += 1
      z -= 1
      t = t[2:]

  point = (x, y, z)
  if point in blacks:
    blacks.remove(point)
  else:
    blacks.add(point)

print(len(blacks))

for _ in range(100):
  # step
  new_blacks = set()
  whites = set()
  for (x, y, z) in blacks:
    for (dx, dy, dz) in ((1,-1,0), (0,-1,1), (-1,0,1), (-1,1,0), (0,1,-1), (1,0,-1)):
      whites.add((x+dx, y+dy, z+dz))

  for (x, y, z) in blacks.union(whites):
    nbrs = 0
    for (dx, dy, dz) in ((1,-1,0), (0,-1,1), (-1,0,1), (-1,1,0), (0,1,-1), (1,0,-1)):
      if (x+dx, y+dy, z+dz) in blacks:
        nbrs += 1

    if (x, y, z) in blacks and (nbrs == 1 or nbrs == 2):
      new_blacks.add((x, y, z))
    if (x, y, z) not in blacks and nbrs == 2:
      new_blacks.add((x, y, z))

  blacks = new_blacks

print(len(blacks))
