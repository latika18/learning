#Find LCM (Lowest Common Multiple) of two numbers a, b
#Example Inputs  >>> 9, 3 o/p  9
#                 >>> 10, 75  o/p 150
#                >>> 190, 51 o/p 9690

#Using the LCM formula LCM = a*b / gcd(a,b)
def LCM(x , y):
    """ define a function LCM which takes two integer inputs and return their LCM using the formula LCM(a,b) = a*b / gcd(a,b) """
    if x==0 or y == 0:
        return "0"
    
    return (x * y)/GCD(x,y)

def GCD(a , b):
    """ define a function GCD which takes two integer inputs and return their common divisor""" 
    com_div =[1]
    i =2
    while i<= min(a,b):
        if a % i == 0 and  b % i ==0:
            com_div.append(i)
        i = i+1
    return com_div[-1]
    
print LCM(350,1)
print LCM(920,350) 
            
