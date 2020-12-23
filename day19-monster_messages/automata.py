import sys

raw_rules, cases = open(sys.argv[1]).read().strip().split("\n\n")

# for r in rules:
#   print(r, '->',rules[r])

rules = {} # of the grammar
for r in raw_rules.split("\n"):
  rule, value = r.split(": ")
  rule = int(rule)
  if rule == 8:
    value = "42 | 42 8"
  if rule == 11:
    value = "42 31 | 42 11 31"
  rules[rule] = value

def consume(case, rule_id):
  # print(case, rule_id)
  rule = rules[rule_id]
  if rule[0] == '"':
    # found terminal symbol
    rule = rule.strip('"')
    if case.startswith(rule):
      return [len(rule)]
    else:
      return []

  bret = []
  for branch in rule.split(' | '):
    acc = [0]
    for rule_id in branch.split(" "):
      nacc = []
      rule_id = int(rule_id)
      for ac in acc:
        ret = consume(case[ac:], rule_id)
        for c in ret:
          nacc.append(c + ac)
      acc = nacc
    bret += acc

  return bret

acc = 0
for word in cases.split("\n"):
  acc += len(word) in consume(word, 0)
print(acc)
