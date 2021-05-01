from collections import Counter
import sys
# integer to binary string of 36 bits => "{:036b}".format(*NUM*)
# binary string to integer => int (STR, 2)


def genMask(line):
    return {pos:line[2][pos] for pos in range(36) if line[2][pos] != 'X'}


def applyMask(value, mask):
    value_list = list(value)
    for k, v in mask.items():
        value_list[k] = v
    return int(''.join(value_list), 2)


def firstStar(instructions):
    # Memory (dictionary allows update and insertion of elements)
    mem = {}
    # Mask (dictionary[ pos (str) : bit (int) ])
    maskDict = {}
    for line in instructions:
        if (line[0] == 'mask'):
            # Generate mask (only useful elements)
            maskDict = genMask(line)
        else:
            memDir = line[0][4:-1]
            memValue = applyMask("{:036b}".format(int(line[2])),
                                 maskDict)
            mem[memDir] = memValue
    return sum([x for x in mem.values() if x != 0])


def main():
    instructions = [x.split(' ')
                    for x in open(sys.argv[1],'r').read().split('\n')[:-1]]
    print("1st STAR SOLUTION ->", firstStar(instructions))


if __name__ == "__main__":
    main()
