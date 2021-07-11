import copy
import sys


def adj_coords(x, y, dims):
    adj = [(x-1, y-1), (x-1, y), (x-1, y+1),
           (x,   y-1),           (x,   y+1),
           (x+1, y-1), (x+1, y), (x+1, y+1)]
    return [(a,b) for a,b in adj
            if a in range(dims[0]) and b in range(dims[1])]


def visible_seats(x, y, prev_gen, dims):
    #  \ | /
    # <- . ->
    #  / | \
    visSeats = []
    # Left upper diagonal seats (\)
    for n in range(1,min(dims[0], dims[1])):
        x_k = x - n
        y_k = y - n
        if (x_k not in range(dims[0]) or y_k not in range(dims[1])):
            visSeats.append((x-1, y-1))
            break
        if (prev_gen[x_k][y_k] != '.'):
            visSeats.append((x_k, y_k))
            break
    # Upper seats (|))
    for n in range(1,dims[0]):
        x_k = x - n
        if (x_k not in range (dims[0])):
            visSeats.append((x-1, y))
            break
        if (prev_gen[x_k][y] != '.'):
            visSeats.append((x_k, y))
            break
    # Right upper diagonal seats (/)
    for n in range(1,min(dims[0], dims[1])):
        x_k = x - n
        y_k = y + n
        if (x_k not in range (dims[0]) or y_k not in range(dims[1])):
            visSeats.append((x-1, y+1))
            break
        if (prev_gen[x_k][y_k] != '.'):
            visSeats.append((x_k, y_k))
            break
    # Left seats (<-)
    for n in range(1,dims[1]):
        y_k = y - n
        if (y_k not in range(dims[1])):
            visSeats.append((x, y-1))
            break
        if (prev_gen[x][y_k] != '.'):
            visSeats.append((x, y_k))
            break
    # Right seats (<-)
    for n in range(1,dims[1]):
        y_k = y + n
        if (y_k not in range(dims[1])):
            visSeats.append((x, y+1))
            break
        if (prev_gen[x][y_k] != '.'):
            visSeats.append((x, y_k))
            break
    # Bottom left diagonal seats (/)
    for n in range(1,min(dims[0], dims[1])):
        x_k = x + n
        y_k = y - n
        if (x_k not in range (dims[0]) or y_k not in range(dims[1])):
            visSeats.append((x+1, y-1))
            break
        if (prev_gen[x_k][y_k] != '.'):
            visSeats.append((x_k, y_k))
            break
    # Bottom seats (|)
    for n in range(1,dims[0]):
        x_k = x + n
        if (x_k not in range (dims[0])):
            visSeats.append((x+1, y))
            break
        if (prev_gen[x_k][y] != '.'):
            visSeats.append((x_k, y))
            break
    # Bottom left diagonal seats (\)
    for n in range(1,min(dims[0], dims[1])):
        x_k = x + n
        y_k = y + n
        if (x_k not in range (dims[0]) or y_k not in range(dims[1])):
            visSeats.append((x+1, y+1))
            break
        if (prev_gen[x_k][y_k] != '.'):
            visSeats.append((x_k, y_k))
            break
    return [(a,b) for a,b in visSeats
            if a in range(dims[0]) and b in range(dims[1])]


def count_neighbours(adjSeats, prev_gen):
    n_neigh = 0
    for i,j in adjSeats:
        if (prev_gen[i][j] == '#'):
            n_neigh += 1
    return n_neigh


def newGen(prev_gen, dims, star, maxSeats):
    new_gen = copy.deepcopy(prev_gen)
    nChgs = 0
    for x in range(dims[0]):
        for y in range(dims[1]):
            # Floor doesnt change, so skip
            if prev_gen[x][y] == '.':
                continue
            # Get adjacent seats
            if star == 1:
                adjSeats = adj_coords(x, y, dims)
            else:
                adjSeats = visible_seats(x, y, prev_gen, dims)
            # Get number of neighbours
            n_neigh = count_neighbours(adjSeats, prev_gen)
            # Apply change to seat
            if prev_gen[x][y] == 'L' and n_neigh == 0:
                new_gen[x][y] = '#'
                nChgs += 1
            elif prev_gen[x][y] == '#' and n_neigh >= maxSeats:
                new_gen[x][y] = 'L'
                nChgs += 1
    return new_gen, nChgs


def main():
    # Read input ( List[List[int]] )
    seats_1st = [list(x) for x in open(sys.argv[1], 'r').read().split('\n')[:-1]]
    seats_2nd = copy.deepcopy(seats_1st)
    # Dimensions of the plane
    dims = [len(seats_1st), len(seats_1st[0])]
    # FIRST STAR
    nChgs_1st = 1
    while(nChgs_1st != 0):
        seats_1st, nChgs_1st = newGen(seats_1st, dims, 1, 4)
    seats_1st_flatten = [y for x in seats_1st for y in x]
    print("1st STAR SOLUTION ->", seats_1st_flatten.count('#'))
    # SECOND STAR
    nChgs_2nd = 1
    while (nChgs_2nd != 0):
        seats_2nd, nChgs_2nd = newGen(seats_2nd, dims, 2, 5)
    # Flatten list to count all accupied seats
    seats_2nd_flatten = [y for x in seats_2nd for y in x]
    print("2nd STAR SOLUTION ->", seats_2nd_flatten.count('#'))


if __name__ == "__main__":
    main()
