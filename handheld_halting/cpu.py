import sys

def loop(instructions):
    seen = set()
    acc, i = 0, 0

    while i >= 0 or i < len(instructions):
        if i in seen:
            return False, acc

        seen.add(i)

        if i >= len(instructions):
            return True, acc

        op, value = instructions[i][0], instructions[i][1]
        if op == 'nop':
            pass
        elif op == 'acc':
            acc += value
        elif op == 'jmp':
            i += value
            continue
        else:
            print('got invalid instruction %s' % op)
            exit(-1)

        if i >= len(instructions) or i + 1 >= len(instructions):
            return True, acc
        i += 1

    return True, acc

def main():
    instructions = []
    for line in open(sys.argv[1]).readlines():
        op, value = line.rstrip().split()
        value = int(value)
        instructions.append((op, value))

    for i, instruction in enumerate(instructions):
        changed = instructions.copy()

        if instruction[0] == 'jmp':
            changed[i] = ('nop', instruction[1])
            halted, acc = loop(changed)
            if halted:
                print(acc)
                break

            
        elif instruction[0] == 'nop':
            changed[i] = ('jmp', instruction[1])
            halted, acc = loop(instructions)
            if halted:
                print(acc)
                break

main()
