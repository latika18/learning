
##Write code to print nth to last elem of linked list


class Node(object):
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,data):
        node = Node(data)
        self.size += 1
        node.next = self.head
        self.head = node

    def print_ntolast(self, n):
        current = self.head
        count = 0
        while current :
            if count == n:
                while current:
                    print current.data
                    current = current.next
                break
            else:
                count += 1
                current = current.next
                print "count = ", count

    def print_data(self):
        current = self.head
        while current:
            print current.data
            current = current.next

New_list = LinkedList()
New_list.insert(10)
New_list.insert(20)
New_list.insert(30)
New_list.insert(40)
New_list.insert(10)
New_list.insert(40)
New_list.print_data()
New_list.print_ntolast(3)
