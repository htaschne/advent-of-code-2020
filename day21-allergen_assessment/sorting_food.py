
relation = {}
allergens = []
ingridients = []
for line in open("out").readlines():
  ingredient, allergen = line.split()
  relation[ingredient] = allergen
  allergens.append(allergen)
  ingridients.append(ingredient)

ingridients = sorted(ingridients)
for i in ingridients:
  print(relation[i], end=',')
print()
