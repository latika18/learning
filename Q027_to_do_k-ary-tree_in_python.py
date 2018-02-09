
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 

def binary_search_tree(input_array):
    """creates a binary search tree representation of a given array"""
   
    binary_tree = []
    
    #Base case when array is empty
    if (len(input_array)) == 1:
        return binary_tree 
    else :
        print binary_tree
        root = Node(input_array[0])
        input_array.pop(0)
        binary_tree.append(root)
        
        if root >= input_array[0]:
            
            root.left = input_array[0]
            input_array.pop(0)
            binary_tree.append(root.left)
            for j in range(len(input_array)-1):
                print binary_tree 
                if root <= input_array[j]:
                    root.right = input_array[j]
                    input_array.pop(j)
                    binary_tree.append(root.right)
                    print binary_tree 
                    break
        elif root <= input_array[0]:
            print binary_tree 
            root.right = input_array[0]
            input_array.pop(0)
            binary_tree.append(root.right)
            for j in range(len(input_array)-1):
                if root >= input_array[j]:
                    root.left = input_array[j]
                    input_array.pop(j)
                    binary_tree.append(root.left)
                    print binary_tree 
                    break   
           
        return binary_search_tree(input_array)



array = [100,12,98,223,-78,-12,82,96,74,30,789,912,120]
print binary_search_tree(array)
