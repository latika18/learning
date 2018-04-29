##Question 14
##Implement a singly linked list in python. You will need to define a class for a node, and create newer objects to hold new values.
##Assume that your data will be like
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501

import pdb
class Node(object):

    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):

    def __init__(self, seq=None):
        self.head = Node()
        self.size =0
        if seq is not None:
            self.extend(seq)
      

    def extend(self, seq):
        """extends list with the given sequence"""
        node = self.head
        for i in range(0, len(seq)):
            node = Node(seq[i],node.next)
            print node.data
            self.size +=1
            node.next = node

    def append(self, a):
        """append string a to the end of list"""
        node = self.head
        while node:
            if node.next == None:
                node = Node(a,node.next)
                self.size +=1
                break
                
            
    def printdata(self):
        """print elements of linked list"""
        node = self.head
        while node:
            pdb.set_trace()
            print node.data
            node = node.next


    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    
    def __contains__(self, item):
        """checks whether given item in list"""
        node = self.head
        pdb.set_trace()
        while node:
            if item == node.data:
                return True
            else:
                return False

    def len(self):
        """returns the length of list"""
        return self.size
    
    def __str__(self):
        return  str(self.data) + str(self.size)


    def remove(self, item):
        """removes item from list"""
        node = self.head
        for node in self:
            if node== item:
                node= node.next
            
        
                
            

if __name__ == "__main__":

    llist = LinkedList([98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24])
    
    print llist.len()
    llist.extend([])
    llist.append([222])
    llist.printdata()
    
    while True:
        item = int(raw_input("Enter a number to search for: "))

        if item in llist:
            print "It's in there!"
        else:
            print "Sorry, don't have that one"

    
   

