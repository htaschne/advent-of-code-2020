
import sys

from collections import defaultdict

todos = set()
toxic = set()
D = {}
counter = defaultdict(int)
for line in open(sys.argv[1]).readlines():
  foods, allergens = line.rstrip().split(" (contains ")
  allergens = allergens.strip(")").split(", ")
  foods = set(foods.split())
  for f in foods:
    todos.add(f)
    counter[f] += 1
  # print(allergens, foods)
  for allergen in allergens:
    if allergen in D:
      v = D[allergen]
      D[allergen] = v.intersection(foods)
    else:
      D[allergen] = foods

for k, v in D.items():
  for f in v:
    toxic.add(f)

ret = todos - toxic
s = 0
for r in ret:
  s += counter[r]
print(s)

for k, v in D.items():
  print(k, ','.join(v))

# python3 food.py 0.in > out
# solve part II by: python3 sorting_food.py
