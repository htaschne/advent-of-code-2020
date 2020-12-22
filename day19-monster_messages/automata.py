import sys

raw_rules, cases = open(sys.argv[1]).read().strip().split("\n\n")

rules = {} # of the grammar
for r in raw_rules.split('\n'):
  rule, value = r.split(': ')
  rules[int(rule)] = value

# for r in rules:
#   print(r, '->',rules[r])

def consume(case, rule_id):
  rule = rules[rule_id]
  if rule[0] == '"':
    # found terminal symbol
    rule = rule.strip('"')
    if case.startswith(rule):
      return len(rule)
    else:
      return -1

  for branch in rule.split(' | '):
    acc = 0
    for rule_id in branch.split(" "):
      rule_id = int(rule_id)
      ret = consume(case[acc:], rule_id)
      if ret == -1:
        acc = -1
        break
      acc += ret
    if acc != -1:
      return acc
  return -1

acc = 0
for word in cases.split("\n"):
  acc += consume(word, 0) == len(word)
print(acc)
