l = open("input.txt", "r").read().split('\n')[:-1]
foundF = False
foundS = False
for x in l:
    for y in l:
        for z in l:
            if not foundS and (int(x)+int(y)+int(z)==2020):
                print("2nd STAR SOLUTION ->", int(x)*int(y)*int(z))
                foundS = True
                break
        if (not founfF and int(x)+int(y)==2020):
            print("1st STAR SOLUTION ->", int(x)*int(y))
            foundF = True
            break
    if (foundF and foundS):
        break
