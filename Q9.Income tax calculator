#Income Tax Calculator
##Slabs and details:
##0-2.5L: Tax rate 0%
##2.5L-5L: Tax rate 5%
##5L-10L: tax rate 20%
##10L and above: tax rate 30%
##For taxable income above 50L, surcharge of 10% is applicable
##For taxable income above 1Cr, surcharge of 15% is applicable
##Krishi Cess of 3% and Swach Bharat cess of 0.18% is applied on all taxes
##Investments under section 80C are deductible upto 2L
##Investments under section 80D are deductible upto 25K
##HRA is minimum of (60% of annual basic salary component, hra component of package, total rent - 10% of basic salary)
##
##Ask for inputs - total taxable income in an year, basic salary for year, hra component for year, annual total rent paid, investments in section 80C, investments in section 80D
##
##Print final tax to be paid

#income_tax_calculator():
def tax_calculator(gti):
    if gti <= 250000:
        print"No Tax"
    elif gti > 250000 and gti <= 500000 :
        print "tax =" , 0.05 * gti
        
    elif gti > 500000 and gti <= 1000000 :
        print "tax =" , 0.05 * 500000 + 0.2 * gti
        
    elif gti > 1000000 :
        print "tax =" , 0.05 * 500000 + 0.2 * 1000000 + 0.3 * gti
        
    if gti > 5000000 and gti < 10000000:
        print "tax =" , tax + 0.01 * tax
        
    if gti > 10000000:
        print "tax =" , tax + 0.15 * tax
        
#asking for inputs
basic_sal = float(raw_input("Enter your basic salary: "))
hra_recvd = float(raw_input("Enter HRA received : "))
rent = float(raw_input("Enter the annual rent paid: "))
invest_80c = float(raw_input("Enter the invested amount in 80 C : "))
invest_80D = float(raw_input("Enter the invested amount in 80 D : "))
taxableincome = 12*basic_sal+(12*hra_recvd -12* min(hra_recvd , 0.6*12*basic_sal , rent - 0.1*basic_sal))

print taxableincome
gross_taxableincome = taxableincome - (invest_80c+invest_80D)
print gross_taxableincome
print tax_calculator(gross_taxableincome)









        

        
        


