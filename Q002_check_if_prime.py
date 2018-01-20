# Question : Create a simple function that checks if a given number is prime number or not.

#check prime
def checkPrime(x):
    status = True
    for i in range (2, int(x**0.5),2):
        if x % i == 0:
            status = False
    return status
        
        
x = int(raw_input("enter a number : "))
print checkPrime(x)
