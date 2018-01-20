#prime numbers group
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#what is the largest prime factor of the number 439225613177 ?
#Link: https://projecteuler.net/problem=3
                
#check prime
#check prime
def checkPrime(x):
    for i in range (3, int(x**0.5),2):
        if x % i == 0:
            return False
        else:
            return True

      

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


print largest_primefactor(6060610)        
print largest_primefactor(600851475143)
