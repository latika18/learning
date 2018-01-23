##Question 23
##Implement a stack class in Python. It should support 3 APIs:
##stack.top(): prints element at top of stack
##stack.pop(): takes out an element from top of stack
##stack.push(): adds a new element at top of stack

class Stack():

    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)
                
    def top(self):
        if len(self.item) >= 1:
            print self.item[len(self.item) -1]
        else :
            print "Empty list"

    def pop(self):
        if len(self.item) >= 1:
            self.item.pop()
        else:
            raise IndexError 

    def push(self,item):
        self.item.append(item)
        print self.item

   
new_stack = Stack()
new_stack.push(19)
new_stack.push(20)
new_stack.push(119)
new_stack.push(202)
new_stack.push(195)
new_stack.push(205)
new_stack.push(149)
new_stack.push(230)

print new_stack.size()
new_stack.top()
new_stack.pop()
new_stack.top()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.top()
