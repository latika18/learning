# Question 27 Perform breadth first traversal on a BST and print the elements traversed
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST(object):
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        current = self.root
        while current:
            if value > current.value:
                if current.right == None:
                    current.right  = Node(value)
                    break
                else:
                    current = current.right
            else:
                if current.left == None :
                    current.left  = Node(value)
                    break
                else:
                    current = current.left
