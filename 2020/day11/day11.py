import copy
import sys


def newGen(prev_gen, dims):
    new_gen = copy.deepcopy(prev_gen)
    num_changes = 0
    for x in range(dims[0]):
        for y in range(dims[1]):
            # Floor doesnt change
            if prev_gen[x][y] == '.':
                continue
            # X,Y coords of a seat
            adj_coords = [(x-1, y-1), (x-1, y), (x-1, y+1),
                          (x,   y-1),           (x,   y+1),
                          (x+1, y-1), (x+1, y), (x+1, y+1)]
            adj_coords = [(x,y) for x,y in adj_coords
                          if x in range(dims[0]) and y in range(dims[1])]
            n_neigh = 0
            for i,j in adj_coords:
                if (prev_gen[i][j] == '#'):
                    n_neigh += 1
            # Apply change to seat
            if prev_gen[x][y] == 'L' and n_neigh == 0:
                new_gen[x][y] = '#'
                num_changes += 1
            elif prev_gen[x][y] == '#' and n_neigh >= 4:
                new_gen[x][y] = 'L'
                num_changes += 1
    return new_gen, num_changes

def main():
    seats = [list(x) for x in open(sys.argv[1], 'r').read().split('\n')[:-1]]
    dims = [len(seats), len(seats[0])]
    # Loop until no changes are made
    while(True):
        seats, num_changes = newGen(seats, dims)
        if (num_changes == 0):
            break
    # Flatten list to count all accupied seats
    seats_flatten = [y for x in seats for y in x]
    print("1st STAR SOLUTION ->", seats_flatten.count('#'))

if __name__ == "__main__":
    main()
