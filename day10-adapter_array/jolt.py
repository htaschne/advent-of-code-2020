
import sys

from collections import defaultdict

def main():
    bag = sorted([int(line.rstrip()) for line in open(sys.argv[1])])
    jolts = set(bag)
    diffs = defaultdict(int)

    outlet = 0
    while True:
        a, b, c = outlet+1, outlet+2, outlet+3
        if a in jolts:
            diffs[1] += 1
            outlet = outlet+1
        elif b in jolts:
            diffs[2] += 1
            outlet = outlet+2
        elif c in jolts:
            diffs[3] += 1
            outlet = outlet+3
        else:
            break

    diffs[3] += 1
    print(diffs[1] * diffs[3])

main()
