##Question 14
##Implement a singly linked list in python. You will need to define a class for a node, and create newer objects to hold new values.
##Assume that your data will be like
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501

class Node(object):

    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):

    def __init__(self, seq=None):
        self.head = Node()
        if seq is not None:
            self.extend(seq)
      

    def extend(self, seq):
        node = self.head
        for i in range(0, len(seq)):
            node = Node(seq[i])
            print node.data
            node = node.next

    def append(self, a):
        node = self.head
        while node:
            print node.data
            node = node.next
            if node == None:
                node.next = Node(a)


    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __contains__(self, item):
        
        for node in self:
            return item 
     
    
    def __repr__(self):
        return  str(self.data) 


    def remove(self, item):
        node = self.head
        for node in self:
            if node== item:
                node= node.next
            
        
                
            

if __name__ == "__main__":

    llist = LinkedList([98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24])
    llist.extend([204,98,78])
    llist.append([222])
    
    while True:
        item = int(raw_input("Enter a number to search for: "))

        if item in llist:
            print "It's in there!"
        else:
            print "Sorry, don't have that one"

    
   

