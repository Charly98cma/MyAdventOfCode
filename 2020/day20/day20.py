from sys import argv as sys_argv
from math import prod as math_prod


def read_input(file_name: str) -> list[str]:
    return open(file_name, 'r') \
        .read() \
        .strip()\
        .replace(':', '')\
        .replace('Tile ', '')\
        .split('\n\n')


def parse_input(input_data: list[str]) -> dict[int:list[list[str]]]:
    tiles_dict = {}
    for tile in input_data:
        tile_list = tile.split('\n')
        tile_id = int(tile_list[0])
        tiles_dict[tile_id] = [list(x) for x in tile_list[1:]]
    return tiles_dict


def gen_sides(tile_img: list[list[str]]) -> list[str]:
    perms_list = []
    for n in [0, -1]:
    # Top (0) and bottom (-1) edges
        perms_list.append(''.join(tile_img[n]))
        perms_list.append(''.join(tile_img[n][::-1]))
    # Left (0) and right (-1) edges
        side = [x[n] for x in tile_img]
        perms_list.append(''.join(side))
        perms_list.append(''.join(side[::-1]))
    return perms_list


def gen_tiles_sides(tiles_dict: dict[int:list[list[str]]]) -> dict[int:list[str]]:
    tiles_perms = {}
    for tile_id, tile_img in tiles_dict.items():
        tiles_perms[tile_id] = gen_sides(tile_img)
    return tiles_perms


def align_tiles(tiles_perms: dict[int:list[str]]) -> dict[int:list[int]]:
    # Dictionary of the adjacent tiles of each tile
    res = {}
    for t_id, t_p in tiles_perms.items():
        res[t_id] = []
        for tile_id, tile_p in tiles_perms.items():
            # Do not match a tile with itself
            if t_id == tile_id:
                continue
            for x in t_p:
                # If theres a common element, the tiles are adjacent
                if x in tile_p:
                    res[t_id].append(tile_id)
                    break
    return res


def first_star(adj_tiles: dict[int:list[int]]) -> int:
    return math_prod(idx
                     for idx, n_adj in adj_tiles.items()
                     if len(n_adj) == 2)


def main():
    input_data = read_input(sys_argv[1])
    tiles_dict = parse_input(input_data)
    tiles_perms = gen_tiles_sides(tiles_dict)
    adj_tiles = align_tiles(tiles_perms)
    print("1st STAR PROBLEM ->", first_star(adj_tiles))

if __name__ == "__main__":
    main()
