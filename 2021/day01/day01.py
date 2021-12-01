import sys, functools

def parse_line(l): return list(map(list, zip(l, l[1:])))
def parse_line_2(l): return list(map(sum, zip(l, l[1:], l[2:])))

in_list = [int(x) for x in sys.stdin.read().split("\n")[:-1]]
print(functools.reduce(lambda acc, l: acc+1 if l[1] > l[0] else acc, parse_line(in_list), 0))
print(functools.reduce(lambda acc, l: acc+1 if l[1] > l[0] else acc, parse_line(parse_line_2(in_list)), 0))
