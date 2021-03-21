from re import match as reMatch, split as reSplit

# Field 'cid' is optional, so its not on the list of required fields
reqFields = {"byr" : [1920, 2002],
             "iyr" : [2010, 2020],
             "eyr" : [2020, 2030],
             "hgt" : {"cm" : [150, 193], "in" : [59, 76]},
             "hcl" : 6,
             "ecl" : ["amb","blu","brn","gry","grn","hzl","oth"],
             "pid" : 9}


def checkInvalidValues(passport, field):
    res = False
    if field in ["byr", "iyr", "eyr"]:
        # +1 because range doesn't include the max value on the range -> [min, max)
        res = int(passport[field]) in range(reqFields[field][0], reqFields[field][1]+1)
    elif field == "hgt":
        units = passport[field][-2:]
        if units not in reqFields[field]:
            res = False
        else:
            # +1 because range doesn't include the max value on the range -> [min, max)
            res = int(passport[field][:-2]) in range(reqFields[field][units][0], reqFields[field][units][1]+1)
    elif field == "hcl":
        res = reMatch(r'(^#[a-f0-9]{0,6}$)', passport[field]) != None
    elif field == "ecl":
        res = passport[field] in reqFields[field]
    elif field == "pid":
        res = reMatch(r'(^[0-9]{9}$)', passport[field]) != None
    return res


passport = dict()
numValid = 0
invalid = False
for l in open("input.txt", "r"):
    l = l.strip()
    if not l: # Empty lines (check passport)
        for field in reqFields:
            if field not in passport or not checkInvalidValues(passport, field):
                invalid = True
                break
        if not invalid:
            numValid += 1
        # Reset the passport data
        passport = dict()
        # Reset the invalid flag
        invalid = False
    else: # Not empty lines (keep reading fields)
        it = iter(reSplit(r'[:| ]', l))
        for key in it:
            passport[key] = next(it)

print("2nd STAR SOLUTION",numValid)
