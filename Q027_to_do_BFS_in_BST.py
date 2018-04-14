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
     def breadth_first_traversal(self, root=None):
        """In BFS the Node Values at each level of the Tree are traversed before going to next level"""

        to_visit = [root]
        if root:
            to_visit.append(root)
            print root.value
        current = root
        while to_visit:
            current = to_visit.pop(0)
            if current.left:
                print current.left.value
                to_visit.append(current.left)
            if current.right:
                print current.right.value
                to_visit.append(current.right)
          
            
        
               
  
t = BinarySearchTree(100)
t.insert(12)
t.insert(92)
t.insert(112)
t.insert(123)
t.insert(2)
t.insert(11)
t.insert(52)
t.insert(3)
t.insert(66)
t.insert(10)

print "Output of Breadth First Traversal is "
t.breadth_first_traversal(t.root)







                   
