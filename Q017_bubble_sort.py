##Question 15
##Check if an element is present within a linked list or not.
##Assume that your linked list data will be like
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501
##Ask for a number and check if it exists within the linked list


class Node:
    def __init__(self,item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Linkedlist:
    def __init__(self):
        self.head = None

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

llist = Linkedlist()
llist.add_member(23)
llist.add_member(98)
llist.add_member(415)
llist.add_member(123)
llist.add_member(981)
llist.add_member(454)
llist.add_member(213)
llist.add_member(198)
llist.add_member(455)
llist.add_member(253)
llist.add_member(978)
llist.add_member(45)
llist.add_member(203)
llist.add_member(918)
llist.add_member(45)
item = int(raw_input("Enter the number you want to search : "))
print llist.search_member(item)


