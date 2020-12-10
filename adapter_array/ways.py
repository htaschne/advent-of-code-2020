import sys

chains = {}
def run(adapter, bag, mx):
    global chains

    if adapter in chains:
        return chains[adapter]
    if adapter == mx:
        return 1

    ret = 0
    if adapter + 1 in bag:
        ret += run(adapter + 1, bag, mx)
    if adapter + 2 in bag:
        ret += run(adapter + 2, bag, mx)
    if adapter + 3 in bag:
        ret += run(adapter + 3, bag, mx)
    chains[adapter] = ret
    return ret

def main():
    bag = [int(line.rstrip()) for line in open(sys.argv[1])]
    bag.append(0)
    bag.append(max(bag)+3)
    mx = bag[len(bag)-1]
    bag = set(bag)

    ret = run(0, bag, mx)
    print(ret)

main()
