Question 24
Implement a queue class in Python: It should support 3 APIs:
queue.top(): prints current element at front of queue
queue.pop(): takes out an element from front of queue
queue.add(): adds a new element at end of stack
class Queue:
    def __init__(self):
        """initialise a Queue class"""
        self.items = []

    def top(self):
        """returns the current element at front of queue"""
        if self.items:
            return self.items[0]
        else:
            raise Exception("Empty Queue")


    def pop(self):
        """takes out an element from front of queue"""
        if self.items:
            self.items.pop(0)
        else :
            raise Exception("Empty Queue")


    def add(self , item):
        """adds a new element at the end of queue"""
        self.items.append(item)


queue_1 = Queue()
queue_1.add(12)
queue_1.add(11)
queue_1.add(55)
queue_1.add(66)
queue_1.add(56)
queue_1.add(43)
queue_1.add(33)
queue_1.add(88)
queue_1.add(56)
queue_1.add(34)
print queue_1
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
print queue_1.top()
queue_1.pop()
