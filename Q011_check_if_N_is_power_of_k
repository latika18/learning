#Question 11 : Check if a number N is a power of k or not.
#Example Inputs :9, 3 #True //3**2 = 9
#                10, 2 #False
#               4096, 16 #True //16**3 = 4096

def check_Power(N,k):
    if N <= 0 or k <=0:
        print "not a valid input"
    else:
        for i in range (1,20):
            x = k**i
            if x == N :
                print " True "
                print k, "power ", i , "is", N
                break
            elif x> N:
                print "false"
                break
        
            
check_Power(244140625,5)
check_Power(4096, 16)
check_Power(0, 16)
check_Power(1,1)








