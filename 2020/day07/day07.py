import sys

def genRules():
    # rules format => ['X', '1 Y', '2 Z']
    return [rule.split(';') for rule in open(sys.argv[1],'r').read()
         .replace(' bags','').replace(' bag','').replace('.','').replace('no other','0 null')
         .replace(' contain ', ';').replace(', ',';')
         .split('\n')][:-1]

def modRules(rules):
    # mydict -> {'X': {'Y': 1, 'Z': 2}}
    myDict = dict()
    for rule in rules:
        # The 2 on 'y[2:]' is to ignore the number and the space next to it :D
        myDict[rule[0]] = {y[2:] : int(y[0]) for y in rule[1:]}
    return myDict

def firstStar(bags, myDict):
    for y in bags:
        for x in myDict:
            if y in myDict[x] and x not in bags:
                bags.append(x);
    return bags

def secondStar(bag, myDict):
    res = 1
    for b in myDict[bag]:
        if b == "null":
            return 1
        else:
            res = res + myDict[bag][b]*secondStar(b,myDict)
    return res


def main():
    bags = ['shiny gold']
    myDict = modRules(genRules())
    print("1st STAR SOLUTION ->", len(firstStar(bags, myDict)[1:]))
    print("2nd STAR SOLUTION ->", secondStar('shiny gold', myDict)-1)

if __name__ == "__main__":
    main()
