import sys

def leGame(numList: list[int], nth: int) -> int:
    """
    Returns the nth number of the game

    Parameters
    ----------
    numList : list[int]
      List of initial values
    nth : int
      Max turn in which the last spoken number is the result

    Returns
    -------
    int
      nth spoken number of the game
    """

    # Create dictionary with initial numbers
    spokenNumbers = { num:turn+1 for turn, num in enumerate(numList) }
    # Get last initial number
    lastNumber = numList[-1]
    # Loop trough each turn
    for turn in range(len(numList), nth):
        if (lastNumber not in spokenNumbers):
            # If new number, add it and say 0
            spokenNumbers[lastNumber] = turn
            lastNumber = 0
        else:
            # If number isn't new, update the turn in which has been spoken
            lastNumber_turn = spokenNumbers[lastNumber]
            spokenNumbers[lastNumber] = turn
            # Say new number based on the age of the last
            lastNumber = turn - lastNumber_turn
    return lastNumber


def main():
    numList = [ int(x) for x in open(sys.argv[1], 'r').read().strip().split(',')]
    print("1st STAR SOLUTION ->", leGame(numList, 2020))
    print("2nd STAR SOLUTION ->", leGame(numList, 30000000))


if __name__ == "__main__":
    main()
