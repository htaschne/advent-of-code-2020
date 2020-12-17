
import sys

def apply_rule(t, rules):
  for r in rules:
    if (t >= r[0] and t <= r[1]) or (t >= r[2] and t <= r[3]):
      return True
  return False

def check(ticket, rules):
  ret = 0
  for i in range(len(ticket)):
    t = ticket[i]
    if not apply_rule(t, rules):
      ret += t
  return ret

# parsing
lines = [line.rstrip() for line in open(sys.argv[1])]

i = 0

# rules
rules = []
RR = {}
while lines[i] != '':
# departure location: 29-458 or 484-956
  r1, r2 = lines[i].split(': ')[1].split(' or ')
  r1 = list(map(int, r1.split('-')))
  r2 = list(map(int, r2.split('-')))
  rules.append((r1[0], r1[1], r2[0], r2[1]))
  RR[i] = (r1[0], r1[1], r2[0], r2[1])
  i += 1

i += 1 # empty line
i += 1 # "your ticket:"

myticket = list(map(int, lines[i].split(',')))
# print(myticket)

i += 1 # empty line
i += 1 # "nearby tickets:"

# following tickets
i += 1
s = 0

tickets = []
while i < len(lines):
  ticket = list(map(int, lines[i].split(',')))
  c = check(ticket, rules)
  if c > 0:
    s +=c
  else:
    tickets.append(ticket)
  # print(ticket)
  i += 1

print(s)
# print(tickets)

def rulex(t, rules):
  itx = []
  for i in range(len(rules)):
    r = rules[i]
    if (t >= r[0] and t <= r[1]) or (t >= r[2] and t <= r[3]):
      itx.append(i)
  return itx

def checkx(ticket, rules):
  ret = 0
  for i in range(len(ticket)):
    t = ticket[i]
    # print(i, rulex(t, rules))
    rr = rulex(t, rules)
    if len(rr) != 0:
      for k in range(len(ticket)):
        if k not in rr:
          print("space", i, "(", t, ")", "can't match rule", k)

for t in tickets:
  checkx(t, rules)

