Do a breadth first traversal on a k-ary tree and print the elements traversed
Example input:
1-> 2
1-> 3
1-> 4
2-> 5
2-> 6
3-> 7
6-> 8

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST(object):
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, value):
        current = self.root
        while current:
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
