# Question : Create a simple function that checks if a given number is prime number or not.

def checkPrime(x):
    flag=0
    for i in range (2,x-1):
        if x % i ==0:
            flag = 1+ flag
        else:
            flag = 0 + flag

    if flag == 0:
        print "prime"
    else:
        print"non prime"

        
x = int(raw_input("enter a number : "))
checkPrime(x)
