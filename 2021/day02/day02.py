#!/usr/bin/env python3
from sys import stdin

stats_1st = {"forward": 0, "depth": 0}
stats_2nd = {"forward": 0, "depth": 0, "aim": 0}

def main():
    for line in stdin:
        mov, n_chg = line.strip().split(" ")
        n_chg = int(n_chg)
        if mov == "forward":
            stats_1st["forward"] += n_chg
            stats_2nd["forward"] += n_chg
            stats_2nd["depth"] += stats_2nd["aim"] * n_chg
        elif mov == "up":
            stats_1st["depth"] -= n_chg
            stats_2nd["aim"] -= n_chg
        else:
            stats_1st["depth"] += n_chg
            stats_2nd["aim"] += n_chg
    print("First star : {}".format(stats_1st["forward"] * stats_1st["depth"]))
    print("Second star : {}".format(stats_2nd["forward"] * stats_2nd["depth"]))


if __name__ == "__main__":
    main()
