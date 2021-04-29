import sys, math

def firstStar(myTS, busesTS):
    divs = [myTS/bus for bus in busesTS]
    minDivs = min(divs)
    myBusID = busesTS[divs.index(minDivs)]
    return ((math.ceil(minDivs) * myBusID) - myTS)*myBusID

def main():
    with open(sys.argv[1],'r') as f:
        myTS = int(f.readline())
        busesTS = [int(x) for x in f.readline().strip().split(',') if x != 'x']
    print("1st STAR SOLUTION ->", firstStar(myTS, busesTS))

if __name__ == "__main__":
    main()
