##Remove duplicastes from linked list without using duplicates
##Write code to remove duplicates with using additional buffer from an unsorted linked list


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

    def remove_dup(self):
        current = self.head
        
        while current is not None:
            second = current.next
            while second is not None:
                if current.data == second.data:
                    second = second.next
                    current.next = second
                else:
                    second = second.next
            current = current.next

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
New_list.remove_dup()
New_list.print_data()

