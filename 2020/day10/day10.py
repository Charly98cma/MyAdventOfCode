 #!/usr/bin/python
import sys

#2nd STAR SOLUTION
class Node:
    def __init__(self, value, left=None, center=None, right=None):
        self.value = value
        self.left = left
        self.center = center
        self.right = right


    def treeLen(self):
        treeL = 1
        if self.left:
            treeL = treeL + 1 + self.left.treeLen()
        if self.right:
            treeL = treeL + 1 + self.right.treeLen()
        if self.center:
            treeL = treeL + 1 + self.center.treeLen()
        if self.left == None and self.center == None and self.right == None:
            return 1
        return treeL

    def insert(self, data):
        if self.value+1 == data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left = self.left.insert(data)
        elif self.value+2 == data:
            if self.center is None:
                self.center = Node(data)
            else:
                self.center = self.center.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right = self.right.insert(data)

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value),
        if self.center:
            self.center.printTree()
        if self.right:
            self.right.printTree()


def firstStar(adapters):
    tree = Node(0)
    outlet = 0
    diffs = [0, 1]
    treeL = 0
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
        tree.insert(outlet)
    return diffs, tree


def main():
    adapters = [int(x) for x in open(sys.argv[1], 'r').read().split('\n')[:-1]]
    diffs, tree = firstStar(adapters)
    print("1st STAR SOLUTION ->", diffs[0]*diffs[1])
    tree.printTree()
    # print("2nd STAR SOLUTION ->", tree.treeLen())

if __name__ == "__main__":
    main()
