##Write code to remove duplicates from an unsorted linked list
class Node(object):
    def __init__(self,data, next=None):
        self.data= data
        self.next = next
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def extend(self,seq):
        """extends list with the give sequence"""
        for item in seq:
            node = Node(item)
            self.size += 1
            node.next = self.head
            self.head = node

    def remove_dup(self):
        stack = []
        
        prev = self.head
        current = self.head.next
        prev.next = current
        
        while current:
            stack.append(current.data)
            current = current.next
            
