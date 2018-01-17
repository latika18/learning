##A palindromic number reads the same both ways. 
##The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##Find the largest palindrome made from the product of two 3-digit numbers.
##Find the largest palindrome made from the product of two 4-digit numbers.Link: https://projecteuler.net/problem=4

def check_palindrome(s):
     if s == s[::-1]:
        return True
product_pal = []
for i in range (999,900,-1):
    for j in range (999,900,-1):
        product = i * j
        if check_palindrome(str(product)):
            product_pal.append(product)
            print"i =" , i , "j = ",j, "for", product
print max(product_pal)


