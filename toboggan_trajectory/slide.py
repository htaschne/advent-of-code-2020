
def main():
  G = [line.rstrip() for line in open('0.in').readlines()]
  ym, xm = len(G), len(G[0])

  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

  ret = 1
  for dx, dy in slopes:
    ret *= slide(G, xm, ym, dx, dy)

  print(ret)

def slide(G, xm, ym, dx, dy):
  x = 0
  y = 0
  ret = 0
  while y < ym:
    x = (x + dx) % xm
    y += dy
    if y >= ym or x >= xm: # why tho?
      break
    if G[y][x] == '#':
      ret += 1
  return ret

if __name__ == '__main__':
  main()

