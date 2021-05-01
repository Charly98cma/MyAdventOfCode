import sys
# integer to binary string of 36 bits => "{:036b}".format(*NUM*)
# binary string to integer => int (STR, 2)


def genMask(line: list[str]) -> dict[int:str]:
    return {pos:line[2][pos]
            for pos in range(36)
            if line[2][pos] != 'X'}


def applyMask(value: str, mask: dict[int:str]) -> int:
    # Turn string to list for easy replacement of elements
    value_list = list(value)
    # Apply each useful bit of the mask
    for k, v in mask.items():
        value_list[k] = v
    # Return the new value as an int
    return int(''.join(value_list), 2)


def firstStar(instructions: list[list[str]]) -> int:
    # Memory (dictionary allows update and insertion of elements)
    mem = {}
    # Mask (dictionary[ pos (str) : bit (int) ])
    maskDict = {}
    for line in instructions:
        if (line[0] == 'mask'):
            # Generate mask (only useful elements)
            maskDict = genMask(line)
        else:
            # Read direction of memory
            memDir = line[0][4:-1]
            # Get value with mask applied
            memValue = applyMask("{:036b}".format(int(line[2])),
                                 maskDict)
            # Add/Replace value to/on memory
            mem[memDir] = memValue
    # Return the sum of all values on memory
    return sum(mem.values())


def main():
    instructions = [x.split(' ')
                    for x in open(sys.argv[1],'r').read().split('\n')[:-1]]
    print("1st STAR SOLUTION ->", firstStar(instructions))


if __name__ == "__main__":
    main()
