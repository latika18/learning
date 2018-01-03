###Create an EMI calculator for loan. Given a principal amount, rate of interest, ask for monthly or quarterly installment terms,
###and take duration of loan in months/years and print EMI amount. Search internet for formula for calculating EMI
###Input format:Principal, Rate of Interest per year, M/Q for Monthly or quarterly installment, duration of year in Year (Y) or Month (M)
###Example Inputs:10000, 12, M, 2Y
### Principal = 10000, Rate of Interest = 12%, Monthly installment, Duration = 2 years
###50000, 10.5, Q, 36M
### Principal = 50000, Rate of Interest = 10.5%, Quarterly installment, Duration = 36 months

def EMI_calculator(P,R , M,d):
#set rate of interest monthly
    print type(R)
    r= (R/(12.0 *100))
    print r
#chechk if monthly or quaterly installment
    if M== 'Q': 
        x=4
    else:
        x=1

    if d[-1] =='Y':
        print "duration in years"
        n = d[0:(len(d)-1)]
        print n
        m = 12 *int(n)
        print m
    elif d[-1] =='M':
        print "duration is in months"
        n = d[0:(len(d)-1)]
        print n   
        m = 1 *int(n) 
        print m
             
    EMI = x*(P*r*(1+r)**m)//((1+r)**m - 1)
    return EMI


print EMI_calculator(10000,12,'Q','3Y')

