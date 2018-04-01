##Question 25
##Create a binary search tree representation of given array of integers.
##Example Input:
##100,12,98,223,-78,-12,82,96,74,30,789,912,120

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

 
