 #Python Script to Implement two stacks in a list
class twoStacks:
     
    def __init__(self, n):     #constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size
         
    # Method to push an element x to stack_1
    def push1(self, x):
         
        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1 :
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
 
        else:
            print("Stack Overflow ")
            exit(1)
 
    # Method to push an element x to stack_2
    def push2(self, x):
 
        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
 
        else :
           print("Stack Overflow ")
           exit(1)
 
    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 -1
            return x
        else:
            print("Stack Underflow ")
            exit(1)
 
    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
            exit()
 
# Driver program to test twoStacks class
ts = twoStacks(15)
ts.push1(15)
ts.push2(30)
ts.push2(15)
ts.push1(12)
ts.push2(7)
 
print("Popped element from stack_1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack_2 is " + str(ts.pop2()))
 
