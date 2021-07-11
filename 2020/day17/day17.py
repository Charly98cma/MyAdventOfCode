#!/usr/bin/env python

from sys import argv as sysArgv
from math import floor as mFloor
from collections import Counter


def get_init_state() -> list[list[str]]:
    init_state = [list(line)
                  for line in open(sysArgv[1], 'r').read().split('\n')[:-1]]
    dims = len(init_state)
    return init_state, dims


def insert_init_state(cube, init_state, num_cycles, layer):
    for num_line, line in enumerate(init_state):
        for num_el, element in enumerate(line):
            # cube[layer][num_cycles+num_line][num_cycles+num_el] = element
            cube[layer][layer][num_cycles+num_line][num_cycles+num_el] = element


def init_cube(initState, dims, num_cycles):
    side, height = dims
    # cube = [[['.' for element in range(side)]
    #          for line in range(side)]
    #         for layer in range(height)]
    cube = [[[['.' for element in range(side)]
              for line in range(side)]
             for element_w in range(height)]
            for layer in range(height)]
    insert_init_state(cube, initState, num_cycles, mFloor(height/2))
    return cube


def get_neighbours(cube, coords, dims):
    # z, y, x = coords
    z, w, y, x = coords
    side, height = dims
    adj_coords = []
    # (-1,2) === [-1, 2) == [-1,1]
    for a in range(-1,2):
        for b in range(-1,2):
            for c in range(-1,2):
                # if (a == 0 and b == 0 and c == 0):
                #     continue
                # adj_coords.append((z+a, y+b, x+c))
                for d in range(-1,2):
                    if (a == 0 and b == 0 and c == 0 and d == 0):
                        continue
                    adj_coords.append((z+a, w+d, y+b, x+c))

    # return len([0 for c, b, a in adj_coords
    #             if c in range(height) and
    #             b in range(side) and
    #             a in range(side) and
    #             cube[c][b][a] == '#'])

    return len([0 for c, d, b, a in adj_coords
                if c in range(height) and
                d in range(height) and
                b in range(side) and
                a in range(side) and
                cube[c][d][b][a] == '#'])




def get_changes(cube, dims):
    changes = []
    for num_layer, layer in enumerate(cube):
        for num_w, w in enumerate(layer):
            for num_line, line in enumerate(w):
                for num_elem, element in enumerate(line):
                    num_neigh = get_neighbours(
                        cube,
                        (num_layer, num_w, num_line, num_elem),
                        dims
                    )
                    if (element == '#' and num_neigh not in [2, 3]):
                        # changes.append(((num_layer, num_line, num_elem), '.'))
                        changes.append(((num_layer, num_w, num_line, num_elem), '.'))
                    elif (element == '.' and num_neigh == 3):
                        # changes.append(((num_layer, num_line, num_elem), '#'))
                        changes.append(((num_layer, num_w, num_line, num_elem), '#'))
    return changes


def apply_changes(cube, changes):
    for coords, new_state in changes:
        # coord_z, coord_y, coord_x = coords
        # cube[coord_z][coord_y][coord_x] = new_state
        coord_z, coord_w, coord_y, coord_x = coords
        cube[coord_z][coord_w][coord_y][coord_x] = new_state


def game_loop(cube, dims, num_cycles):
    for n in range(num_cycles):
        changes = get_changes(cube, dims)
        apply_changes(cube, changes)


def count_active_cubs(cube):
    num_cubes = 0
    for layer in cube:
        for layer_w in layer:
            for line in layer_w:
                num_cubes += Counter(line)['#']
    return num_cubes


def print_cube(cube):
    for layer in cube:
        for w in layer:
            print()
            for line in w:
                print(line)
                print()


def main():
    # Number of cycles given by exercise
    num_cycles = 6
    init_state, dims = get_init_state()
    # Create a big enough cube (oversized cube)
    side = 2*num_cycles+dims
    height = 2*num_cycles+1
    # Init cube and add initial values
    cube = init_cube(init_state, (side, height), num_cycles)
    game_loop(cube, (side, height), num_cycles)
    # print("1st STAR SOLUTION ->", count_active_cubs(cube))
    print("2nd STAR SOLUTION ->", count_active_cubs(cube))

if __name__ == "__main__":
    main()
