import sys

bags = ['shiny gold']

# rules format => ['X', '1 Y', '2 Z']
rules = [rule.split(';') for rule in open(sys.argv[1],'r').read()
         .replace(' bags','').replace(' bag','').replace('.','').replace('no other','0 null')
         .replace(' contain ', ';').replace(', ',';')
         .split('\n')][:-1]


# mydict -> {'X': {'Y': 1, 'Z': 2}}
mydict = dict()
for rule in rules:
    # The 2 on 'y[2:]' is to ignore the number and the space next to it :D
    mydict[rule[0]] = {y[2:] : int(y[0]) for y in rule[1:]}


for y in bags:
    for x in mydict:
        if y in mydict[x] and x not in bags:
            bags.append(x);

print("1st STAR SOLUTION ->", len(bags[1:]))
