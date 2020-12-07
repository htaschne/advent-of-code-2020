import sys

from collections import defaultdict

def explore(target, preds):
  global ret, seen, values
  if preds[target] == []:
    return

  for pred in preds[target]:
    seen.add(pred)
    explore(pred, preds)

def bags(target, values):
  if values[target] == []: 
    return 1
  res = 1
  for n, b, c in values[target]:
    res += n * bags((b, c), values) 
  return res 

rules = [line.rstrip() for line in open(sys.argv[1])]

preds, values = defaultdict(list), defaultdict(list)
for i, rule in enumerate(rules):
  # print(i, rule)
  if ',' in rule:
    rule = rule.split(', ')
    b1, c1, _, _, n, b2, c2, _ = rule[0].split(' ')
    preds[(b2, c2)].append((b1, c1))
    values[(b1, c1)].append((int(n), b2, c2))
    rule.pop(0)
    for r in rule:
      # 2 muted yellow bags
      # print('rule: ', r)
      n, b2, c2, _ = r.split(' ')
      preds[(b2, c2)].append((b1, c1))
      values[(b1, c1)].append((int(n), b2, c2))

  elif 'no other bags' in rule:
    # faded blue bags contain no other bags.
    b1, c1, _, _, _, _, _ = rule.split(' ')
    preds[(b1, c1)] = []
    values[(b1, c1)] = []

  else:
    # bright white bags contain 1 shiny gold bag.
    # print(rule.split(' '))
    b1, c1, _, _, n, b2, c2, _ = rule.split(' ')
    preds[(b2, c2)].append((b1, c1))
    values[(b1, c1)].append((int(n), b2, c2))

ret, seen = 0, set() 
explore(('shiny', 'gold'), preds)
print(len(seen))
print(bags(('shiny', 'gold'), values) - 1)
