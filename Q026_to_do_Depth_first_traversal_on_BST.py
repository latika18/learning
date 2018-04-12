###Perform Depth first traversal on a BST and print the elements traversed
###Example Input:
###100,12,98,223,-78,-12,82,96,74,30,789,912,120
# A node structure
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
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right
                    
     
    
    def preorder(self,root):
##        root,left,right
        
      if root:
          print root.value
          if root.left:
                self.preorder(root.left)
          if root.right:
                self.preorder(root.right)
     

    def postorder(self,root):
##      left ,right , root
##        import pdb;pdb.set_trace()
        if root:
            if root.left:
                self.postorder(root.left)
            if root.right:
                self.postorder(root.right)
            print root.value


    def inorder(self,root):
##        leftt,root,right
##        import pdb;pdb.set_trace()
          
        if root.left:
            self.inorder(root.left)
        print root.value
        if root.right:
            self.inorder(root.right)


t = BST(22)
t.insert(30)
t.insert(10)
t.insert(80)
t.insert(90)
t.insert(9)
t.insert(23)
t.insert(14)
t.insert(6)
t.insert(40)
t.insert(60)
t.insert(3)
print "preorder"
t.preorder(t.root)
print "postorder"
t.postorder(t.root)
print "inorder"
t.inorder(t.root)

             
