from sys import stdin
in_list = [int(x) for x in stdin.read().split("\n")[:-1]]
print(len([0 for i in range(len(in_list)-1) if in_list[i] < in_list[i+1]]))
print(len([0 for i in range(len(in_list)-1) if sum(in_list[i:i+3]) < sum(in_list[i+1: i+4])]))
