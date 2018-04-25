##Question 16
##Implement insertion sort in python. Don’t use Python’s built in sort or sorted.
##Make classes for a node, with pointers for next
##Assume your inputs will be sufficient for the memory you have.
##Example inputs
##>>> 11,127,56,2,1,5,7,9,11,65,12,24,76,87,123,65,8,32,86,123,67,1,67,92,72,39,49,12
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501


def insert_sort(a):
    if len(a)== 0:
        print "Please give valid input"
    for i in range(1, len(a)):
        current = 0
        while current < i:
            if a[i] < a[current]:
                a[current], a[i]= a[i] , a[current]
                
            current = current + 1
    return a
  
print insert_sort([12,54,66,43,11,33,34,33,1,45])















        



