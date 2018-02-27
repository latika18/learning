##Question 15
##Check if an element is present within a linked list or not.
##Assume that your linked list data will be like
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501



class Node:
    
    
    def __init__(self, data , next = None):
        self.data = data
        self.next = next

##    def getData(self):
##        return self.data
##
##    def getNext(self):
##        return self.next
##
##    def setData(self,newdata):
##        self.data = newdata
##
##    def setNext(self, newnext):
##        self.next = newnext


class Linkedlist:
    def __init__(self,seq = None):
        self.seq = seq
        if seq != None:
            self.extend(seq)

##    def __contains__(self, item):
##        for i in self:
##        ...

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def add_member(self,data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def search_member(self,item):
        current = self.head
        while current != None:
            if current.getData() ==item:
                return True
            else:
                current =current.getNext()
        return False


llist = Linkedlist([23, 98, 415, 123, 981, 454, 213, 198])

while True:
    item = int(raw_input("Enter a number to search for: "))

    if item in llist:
        print "It's in there!"
    else:
        print "Sorry, don't have that one . Check for another number."
