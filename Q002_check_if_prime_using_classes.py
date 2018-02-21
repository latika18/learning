
#implement a class prime
class prime():
    def __init__(self,num,k):
        self.num = int(num)
        self.k = k

    def check_prime(self):
        
        for i in range (2,self.num/2):
            if self.num % i:
                self.k =1
                break
            
    def show_result(self):
        if self.k == 1:
            print "num is not prime"
        else:
            print "num is prime"
            
##main program

#a = int(raw_input("Enter a number : "))
a = prime(raw_input("Enter a number : ") ,0)

a.check_prime()
a.show_result()     




