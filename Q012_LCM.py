#Find LCM (Lowest Common Multiple) of two numbers a, b
#Example Inputs  >>> 9, 3 o/p  9
#                 >>> 10, 75  o/p 150
#                >>> 190, 51 o/p 9690

def LCM(x , y):
    """ define a function LCM which take two  integerinputs and return their LCM"""
    if x==0 or y == 0:
        return "0"
    multiple_set_1  = []
    multiple_set_2  = []
    for i in range(1,y+1):
        multiple_set_1.append(x*i)
    for j in range(1,x+1):
        multiple_set_2.append(y*j)
    for z in range (1,x*y+1):
        if z in multiple_set_1:
            if z in multiple_set_2:
                return z
                break
    
print LCM(350,450)
