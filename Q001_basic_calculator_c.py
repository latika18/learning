# Question : Create a simple function that given 3 inputs - number 1, number 2 and operator -  calculates the result.
#The function supports DMAS operations, and accepts only integers

def calculate(x , y , op):
    if op == '+' :
        z = x  + y
    elif op == '-' :
        z = x - y
    elif op == '*' :
        z = x * y
    elif op == '//' :
        if y!=0:
            z = x // y
        else:
           raise exception
    return z
print calculate(9 , 9 , '+')
print calculate(9 , 9 , ' -')
print calculate(9 , 9 , ' *')
print calculate(9 , 9 , '//')
print calculate(11 , 0 , '//')

