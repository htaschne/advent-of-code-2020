
import sys

def check(keys):
  must = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

  for m in must:
    if m not in keys:
      return False

  # for part I comment the rest of this function
 

  keys['byr'] = int(keys['byr'])
  a = keys['byr'] >= 1920 and keys['byr'] <= 2002
  if not a:
    return False

  keys['iyr'] = int(keys['iyr'])
  b = keys['iyr'] >= 2010 and keys['iyr'] <= 2020
  if not b:
    return False

  keys['eyr'] = int(keys['eyr'])
  c = keys['eyr'] >= 2020 and keys['eyr'] <= 2030
  if not c:
    return False

  if 'cm' in keys['hgt']:
    vv = int(keys['hgt'][:-2])
    d = vv >= 150 and vv <= 193
    if not d:
      return False
  elif 'in' in keys['hgt']:
    vv = int(keys['hgt'][:-2])
    d = vv >= 59 and vv <= 76
    if not d:
      return False
  else:
    return False

  hh = keys['hcl']
  if '#' not in hh or len(hh) != 7:
    return False

  eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  if keys['ecl'] not in eyes:
    return False

  if len(keys['pid']) != 9:
    return False

  return True

def main():
  res = 0
  for i, line in enumerate(open(sys.argv[1]).readlines()):
    # print(i)
    toks = line.rstrip().split(' ')
    keys = {}
    for tok in toks:
      k, v = tok.split(':')
      keys[k] = v

    ret = check(keys)
    if ret:
      # print(i, keys)
      res += 1

  print(res)


if __name__ == '__main__':
  main()

