import sys

lines = [line.rstrip().split(" ") for line in open(sys.argv[1]).readlines()]
valids = 0
for interval, rule_letter, password in lines:
  rule_letter = rule_letter[:-1]
  lo, hi = [int(x) for x in interval.split("-")]
  validate_count = sum([letter == rule_letter for letter in password])
  if validate_count >= lo and validate_count <= hi:
    valids += 1

print(valids)

valids = 0
for interval, rule_letter, password in lines:
  rule_letter = rule_letter[:-1]
  lo, hi = [int(x) for x in interval.split("-")]
  if (password[lo-1] == rule_letter) ^ (password[hi-1] == rule_letter):
    valids += 1

print(valids)
