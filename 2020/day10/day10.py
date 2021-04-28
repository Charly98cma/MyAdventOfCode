#!/usr/bin/python
from collections import Counter, defaultdict
import sys


def firstStar(adapters):
    return [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]


def secondStar(diffs):
    result = 1
    counter = 0
    # Number of 1 series that produce X lists (num_1 : num_lists)
    mults = {2: 2, 3: 4, 4: 7, 5: 13}
    # Default dictionary for numbers (integers)
    resDict = defaultdict(int)
    # Find the series of 1's on the diffs
    for i in diffs:
        if i == 1:
            counter += 1
        else:
            if counter > 1:
                resDict[counter] += 1
            counter = 0
    if counter > 1:
        resDict[counter] += 1
    # CAlculate the number of different lists
    for i, j in dict(resDict).items():
        result *= mults[i] ** j
    return result


def main():
    adapters = [0] + sorted([int(x) for x in open(sys.argv[1], 'r').read().split('\n')[:-1]])
    diffs = firstStar(adapters)
    countDiffs = Counter(diffs)
    print("1st STAR SOLUTION ->", countDiffs[1]*(countDiffs[3]+1))
    print("2nd STAR SOLUTION ->", secondStar(diffs))

if __name__ == "__main__":
    main()
