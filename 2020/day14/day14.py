import sys


def getMemDir(line: list[str]) -> str:
    """
    Reads and returns the memory direction from the line

    Parameters
    ----------
    line : list[str]
      The instruction/line with the memory direction

    Returns
    -------
    str
      The memory direction
    """

    return line[0][4:-1]



def genMask(line: list[str], mode) -> dict[int:str]:
    """
    Reads the mask from the instruction/line and generates a
    dictionary of the format { pos : value }.
    A certain character is ignored depending on the 3rd argument
    (mode == 0 -> ignore X, mode != 0 -> ignore 0)

    Parameters
    ----------
    line : list[str]
      The instruction/line with the mask
    mode : int
      The mode/star the function has been called from (0-1st, 1-2nd)

    Returns
    -------
    dict[int:str]
      Dictionary with the positions and values of the mask
    """

    ignore_char = 'X' if mode == 0 else '0'
    return {pos:line[2][pos]
            for pos in range(36)
            if line[2][pos] != ignore_char}



def applyMask1st(value: str, mask: dict[int:str]) -> int:
    """
    Apply the mask to the value, replacing some characters on the value
    according to the dictionary.

    Parameters
    ----------
    value : str
      Value in which apply the mask
    mask : dict[int:str]
      Substitution mask represented as a dictionary

    Returns
    -------
    int
      value after applying the mask and being casted to int
    """

    # Turn string to list for easy replacement of elements
    value_list = list(value)
    # Apply each useful bit of the mask
    for k, v in mask.items():
        value_list[k] = v
    # Return the new value as an int
    return int(''.join(value_list), 2)



def applyMask2nd(value: str, mask: dict[int:str]) -> list[str]:
    """
    Apply the mask to the value, replacing some characters on the value
    according to the dictionary.

    Parameters
    ----------
    value : str
      Memory direction in which the mask is applied
    mask : dict[int:str]
      Substitution mask represented as a dictionary

    Returns
    -------
    list[str]
      memory direction after applying the mask
    """

    # Turn string to list for easy replacement of elements
    value_list = list(value)
    # Apply each useful bit of the mask
    for k, v in mask.items():
        value_list[k] = v
    # Return the value as a list to generate all possible directions
    return value_list



def genCombs(nX: int) -> list[list[str]]:
    """
    Given a certain number of X's on the memory direction,
    returns a list with all possible binary number up to 2**num_Xs

    Parameters
    ----------
    nX : int
      Number of X's on the value after applying the mask

    Returns
    -------
    list[list[str]]
      List (of list) of all possible binary number with nX bits
    """

    return [list("{:0b}".format(x).zfill(nX)) for x in range(2**nX)]



def genFloatingDirs(memDir: list[str]) -> list[int]:
    """
    Given a memory diection with some floating bits, generates
    all the possible directions that could be built.

    Parameters
    ----------
    memDir : list[str]
      Memory direction given as a list of strings (each string is one bit)

    Returns
    -------
    list[int]
      List of all possible memory directions
    """

    lenDir = len(memDir)
    allDirs = []
    for x in genCombs(memDir.count('X')):
        memDir_bkp = list(memDir)
        ptrX = 0
        for pos in range(lenDir):
            if (memDir_bkp[pos] == 'X'):
                memDir_bkp[pos] = x[ptrX]
                ptrX += 1
        # When all X replaced, save dir
        allDirs.append(int(''.join(memDir_bkp), 2))
    return allDirs


def secondStar(instructions: list[list[str]]) -> int:
    """
    Solution for the second star.
    The mask is applied to the memory direction, the 0 do not changes bits and
    the X is a floating bit.

    Parameters
    ----------
    instructions : list[list[str]]
      List of instructions, being each one of these a list of each field

    Returns
    -------
    int
      The sum of all values on memory
    """

    # Memory (dictionary allows update and insertion of elements)
    mem = {}
    # Mask (dictionary[ pos (str) : bit (int) ])
    maskDict = {}
    for line in instructions:
        if (line[0] == 'mask'):
            # Generate mask for second (num. 1) star (only useful elements)
            maskDict = genMask(line, 1)
        else:
            # Apply mask to the mem dir and generate all possible directions
            memDir = applyMask2nd("{:036b}".format(int(getMemDir(line))),
                                    maskDict)
            memDir_list = genFloatingDirs(memDir)
            # Read value to be written
            memValue = int(line[2])
            # Write value on all possible directions
            for d in memDir_list:
                mem[d] = memValue
    return sum(mem.values())



def firstStar(instructions: list[list[str]]) -> int:
    """
    Solution for the first star.
    The mask is applied to the memory direction, the X do not changes bits and
    1's and 0 on the mask replace any number on the value.

    Parameters
    ----------
    instructions : list[list[str]]
      List of instructions, being each one of these a list of each field

    Returns
    -------
    int
      The sum of all values on memory
    """

    # Memory (dictionary allows update and insertion of elements)
    mem = {}
    # Mask (dictionary[ pos (str) : bit (int) ])
    maskDict = {}
    for line in instructions:
        if (line[0] == 'mask'):
            # Generate mask for first (num. 0) star (only useful elements)
            maskDict = genMask(line, 0)
        else:
            # Read direction of memory
            memDir = getMemDir(line)
            # Get value with mask applied
            memValue = applyMask1st("{:036b}".format(int(line[2])),
                                    maskDict)
            # Add/Replace value to/on memory
            mem[memDir] = memValue
    # Return the sum of all values on memory
    return sum(mem.values())


def main():
    instructions = [x.split(' ')
                    for x in open(sys.argv[1],'r').read().split('\n')[:-1]]
    print("1st STAR SOLUTION ->", firstStar(instructions))
    print("2nd STAR SOLUTION ->", secondStar(instructions))

if __name__ == "__main__":
    main()
