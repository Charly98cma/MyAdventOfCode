from sys import stdin
def parse_line(l): return list(map(list, zip(l, l[1:])))
in_list = [int(x) for x in stdin.read().split("\n")[:-1]]
print(len([0 for x, y in parse_line(in_list) if y > x]))
print(len([0 for x, y in parse_line(list(map(sum, zip(in_list, in_list[1:], in_list[2:])))) if y > x]))
