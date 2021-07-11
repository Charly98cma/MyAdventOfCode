import sys


def getInput(inputFile):
    # Read input from the file
    with open(inputFile, 'r') as f:
        rules = genRules(f)
        myTicket = getMyTicket(f)
        nearbyTickets = getNearbyTickets(f)
    return rules, myTicket, nearbyTickets


def genRules(f):
    rules = {}
    while True:
        # Read rule line and split name and ranges
        line = f.readline().strip().split(':')
        if (line[0] == ""):
            # End of rules
            break
        # +1 since must be inclusive (ranges arent)
        rules[line[0]] = [
            range(int(y[0]),int(y[1])+1)
            for y in [x.split('-')
                      for x in line[1].split(" or ")]
        ]
    return rules


def getMyTicket(f):
    # Consume "your ticket" line
    f.readline()
    # Read, split, and cast each value of the ticket to int
    return [int(x) for x in f.readline().strip().split(',')]


def getNearbyTickets(f):
    # Consume the empty and "nearby tickets" lines
    f.readline()
    f.readline()
    tickets = []
    # Read each line of the nearby tickets and format them
    for line in f:
        tickets.append([int(x) for x in line.strip().split(',')])
    return tickets


def getErrorRate(allRanges, nearbyTickets):
    errorRate = 0
    # Store invalid lines so they are deleted later
    invalidLines = []
    # Check each ticket value meet at least one of the rules
    for ticket in nearbyTickets:
        for field in ticket:
            # If a value does not meet any range, the ticket is invalid
            if (not any([field in r for r in allRanges])):
                errorRate += field
                invalidLines.append(ticket)
    return errorRate, invalidLines


def does_ticket_meets_range(column, ranges):
    for value in column:
        if (not any(value in r for r in ranges)):
            return False
    return True


def remove_pos_from_possible_positions(possiblePosList, value):
    [l.remove(value) for l in possiblePosList if value in l]


def getFieldPositions(rules, nearbyTickets_zip):
    # Init the definitive positions of each field
    fieldPositions = {}
    # Init each possible field positions
    possiblePositions = { field:[] for field in rules.keys() }
    # Get possible positions of each field
    for pos, column in enumerate(nearbyTickets_zip):
        for field, ranges in rules.items():
            if (does_ticket_meets_range(column, ranges)):
                possiblePositions[field].append(pos)
    # Get number of fields
    nFields = len(rules)
    # Find the columns that match with only one pos and delete that from the
    # rest. Repeat until all positions are assigned
    while len(fieldPositions) != nFields:
        for field, positions in possiblePositions.items():
            # If len of positions is 1, all value of column meet only one rule
            if len(positions) == 1:
                pos = positions[0]
                fieldPositions[field] = pos
                remove_pos_from_possible_positions(possiblePositions.values(), pos)
    return fieldPositions


def getDeparturesProd(positions, myTicket):
    # Get product of all field that start with "departure"
    prod = 1
    for field, pos in positions.items():
        if "departure" in field:
            prod *= myTicket[pos]
    return prod


def main():
    rules, myTicket, nearbyTickets = getInput(sys.argv[1])
    allRanges = [r for rList in rules.values() for r in rList]
    # Get the error rate and the invalid tickets
    errorRate, invalidTickets = getErrorRate(allRanges, nearbyTickets)
    print("1st STAR SOLUTION ->", errorRate)
    # Delete invalid tickets
    [nearbyTickets.remove(ticket) for ticket in invalidTickets]
    # Zip the values of each column for better management
    nearbyTickets_zip = list(zip(*nearbyTickets))
    # Get positions of fields on tickets
    positions = getFieldPositions(rules, nearbyTickets_zip)

    print("2nd STAR SOLUTION ->", getDeparturesProd(positions, myTicket))

if __name__ == "__main__":
    main()
