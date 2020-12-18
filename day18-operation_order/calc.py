
import sys

def evaluate(tok):
  # 1+2*3+...
  cur = int(tok[0])
  for i in range(1, len(tok)):
    if tok[i] == '+':
      r = int(tok[i+1])
      cur = cur + r
    elif tok[i] == '*':
      r = int(tok[i+1])
      cur = cur * r
  return cur

def eval_with_prec(tok):
  while len(tok) > 1:
    hold, toEval = [], []
    done = False

    while not done and len(tok) > 0:
      ch = tok.pop()
      if ch == '+':
        done = True
      hold.append(ch)

    if len(tok) == 0 and not done:
      # no + found
      hold.reverse()
      res = evaluate(hold)
      tok.append(res)
    else:
      toEval.append(tok.pop())
      toEval.append(hold.pop())
      toEval.append(hold.pop())
      toEval.reverse()

      res = evaluate(toEval)
      hold.append(res)

      while len(hold) > 0:
        tok.append(hold.pop())

  return tok[0]

exprs = [l.rstrip().replace('(', '( ').replace(')', ' )').split() for l in open(sys.argv[1]).readlines()]

ret = 0
for exp in exprs:
  s = []
  for ch in exp:
    if ch != ')':
      s.append(ch)
    else:
      toEval = []
      while s[len(s) -1] != '(':
        toEval.append(s.pop())
      s.pop()
      toEval.reverse()

      # r = evaluate(toEval))
      r = eval_with_prec(toEval)
      s.append(r)

  r = 0
  if len(s) > 1:
    # r = evaluate(s)
    r = eval_with_prec(s)
  else:
    r = s[0]

  ret += r
print(ret)

