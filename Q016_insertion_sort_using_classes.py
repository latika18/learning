##Question 16
##Implement insertion sort in python. Don’t use Python’s built in sort or sorted.
##Make classes for a node, with pointers for next
##Assume your inputs will be sufficient for the memory you have.
##Example inputs
##>>> 11,127,56,2,1,5,7,9,11,65,12,24,76,87,123,65,8,32,86,123,67,1,67,92,72,39,49,12
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501


def insert_sort(alist):
    """ Fuction to sort a given list a """
    
    for i in range(0, len(alist)-1):
        current = i+1
        while current :
            ###if the current number is lesser than the number on left than swap values
            if alist[current] < alist[i]:
                alist[current], alist[i] = alist[i], alist[current]
                print alist
            current = current - 1 
            i = i - 1
               
    return alist
  
print insert_sort([11,126,54,2,1,65,24,77,93,31,44,55,20])




















        



