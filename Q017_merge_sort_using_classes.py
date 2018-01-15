##Question 16
##Implement insertion sort in python. Don’t use Python’s built in sort or sorted.
##Make classes for a node, with pointers for next
##Assume your inputs will be sufficient for the memory you have.
##Example inputs
##>>> 11,127,56,2,1,5,7,9,11,65,12,24,76,87,123,65,8,32,86,123,67,1,67,92,72,39,49,12
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501


class Node:

    def __init__(self,data,next = None):
        self.data =data
        self.next = None

class LinkedList:
    def __init__(self, seq=None):
        self.head = Node(None)
        if seq is not None:
            self.head.data = seq
            
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
            
temp = Node(67)
print temp.data

llist = LinkedList([23])s
while True:
    item = int(raw_input("Enter a number to search for: "))

    if item in llist:
        print "It's in there!"
    else:
        print "Sorry, don't have that one."

 











        



