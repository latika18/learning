##Question 14
##Implement a singly linked list in python. You will need to define a class for a node, and create newer objects to hold new values.
##Assume that your data will be like
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501

class Node:

    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:


    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def printList(self):
        current = self.head
        count = 0
        while current != None:
            print current.getData()
            current = current.getNext()
            count = count +1


temp = Node(67)
print temp.getData()
my_list = UnorderedList()
my_list.add(93)
my_list.add(60)
my_list.add(34)
my_list.add(9)
my_list.add(5)
my_list.add(193)
my_list.add(30)
my_list.add(54)
my_list.add(707)
my_list.add(930)
my_list.add(600)
my_list.add(1034)
my_list.add(19)
my_list.printList()
