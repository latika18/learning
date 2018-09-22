class stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        x = len(self.stack)
        stack = self.stack[:x-1]

    def push(self,a):
        self.stack.append(a)

    def printdata(self):
        print self.stack

    def min_value(self):
        min_val = self.stack[0]
        n = 0
       
        while self.stack[n]:
            if min_val > self.stack[n]:
                min_val = x
            n += 1
        return min_val
    

    
    

A = stack()

A.push(3)
A.push(7)
A.push(13)
A.push(17)
A.push(23)
A.push(27)
A.pop()
A.printdata()
A.min_value()



        
