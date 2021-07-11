from sys import argv as sys_argv
from math import ceil as math_ceil


def read_input(input_file):
    with open(input_file, 'r') as f:
        return int(f.readline()), f.readline().strip().split(',')


def first_star(my_ts, buses_keys) -> int:
    divs = [my_ts/bus for bus in buses_keys]
    my_bus_id = buses_keys[divs.index(min(divs))]
    return ((math_ceil(min(divs)) * my_bus_id) - my_ts) * my_bus_id


def secondStar(buses_dict) -> int:
    res = 1
    W = 1
    # Loop through each "equation", finding its module and
    # the next "starting point" (res after each for iteration)
    for bus_id, bus_ts in buses_dict.items():
        while (res + bus_ts) % bus_id != 0:
            res += W
        W *= bus_id
    return res


def main():
    my_ts, buses_ts_str = read_input(sys_argv[1])
    # Dict of the format -> { bus_id : pos_of_bus }
    buses_dict = {int(bus_id): int(bus_ts)
                  for bus_ts, bus_id in enumerate(buses_ts_str)
                  if bus_id != 'x'}
    print("1st STAR SOLUTION ->", first_star(my_ts, list(buses_dict.keys())))
    print("2nd STAR SOLUTION ->", secondStar(buses_dict,))


if __name__ == "__main__":
    main()
