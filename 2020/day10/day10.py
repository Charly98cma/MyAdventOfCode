 #!/usr/bin/python
import sys

adapters = [int(x) for x in open(sys.argv[1], 'r').read().split('\n')[:-1]]
outlet = 0
diffs = [0, 1]
treeL = 0

#2nd STAR SOLUTION
class Node:
    def __init__(self, value, left=None, center=None, right=None):
        self.value = value
        self.left = left
        self.center = center
        self.right = right


    def treeLen(self):
        global treeL
        if self.left:
            self.left.treeLen()
        if self.right:
            self.right.treeLen()
        if self.center:
            self.center.treeLen()
        if self.left == None and self.center == None and self.right == None:
            treeL += 1

tree = Node(0)

# 1st STAR SOLUTION
for x in range(len(adapters)):
    if outlet == max(adapters)+3:
        break
    if outlet+1 in adapters:
        outlet += 1
        diffs[0] += 1
    elif outlet+2 in adapters:
        outlet += 2
    elif outlet+3 in adapters:
        outlet += 3
        diffs[1] += 1
    else:
        print("Error")
        exit(1)

for x in range(len(adapters)):
    tree.insert(outlet)

print("1st STAR SOLUTION ->", diffs[0]*diffs[1])
tree.treeLen()
print("2nd STAR SOLUTION ->", treeL)
