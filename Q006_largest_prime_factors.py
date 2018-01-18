#prime numbers group
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#what is the largest prime factor of the number 439225613177 ?
#Link: https://projecteuler.net/problem=3
                
#check prime
def checkPrime(x):
    flag=0
    for i in range (2,x-1):
        if x % i ==0:
            flag = 1+ flag
        else:
            flag = 0 + flag

    if flag == 0:
        return x
    

#primefactors
def largest_primefactor(x):
        factors = []
        prime_factors = []
        for i in range (2,x-1):
                if x%i ==0:
                        factors.append(i)
        print factors
        for i in factors:
                prime_factors.append(checkPrime(i))
        return max(prime_factors)


print largest_primefactor(606061)        
print largest_primefactor(600851475143)
