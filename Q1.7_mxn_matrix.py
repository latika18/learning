##Write an algorithm such that if an element in mxn matrix is 0, its entire row and columns is set to 0.

a = []
A = [a]
m = int(raw_input("enter the no of rows"))
n = int(raw_input("enter the number of columns"))
for i in range(0,m):
    for j in range(0,n):
        #a[j] = int(raw_input("enter the values"))
        print a[i][j]

print A


