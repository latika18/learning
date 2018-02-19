
# Question : Create a simple function that given 3 inputs - number 1, number 2 and operator -  calculates the result.
#The function supports DMAS operations, and accepts only integers

class calculator():
    
    def __init__(self,value1 , value2, operand):
        self.value1 = int(value1)
        self.value2 = int(value2)
        self.operand = operand

    def calculate (self):
        if self.operand == '+' :
            return self.value1 + self.value2

        if self.operand == '*':
            return self.value1 * self.value2

        if self.operand == '-' :
            return self.value1 - self.value2
    
        if self.operand == '/' :
            if self.value2 == 0:
                raise ZeroDivisionError
            else:
                return self.value1 / self.value2


r = calculator(6,7, '+')
print r.calculate()

r = calculator(3,7, '-')
print r.calculate()

r = calculator(6,0, '*')
print r.calculate()

r = calculator(9,5, '/')
print r.calculate()
