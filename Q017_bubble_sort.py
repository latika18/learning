# -*- coding: cp1252 -*-
##Implement bubble sort in python. Don’t use Python’s built in sort or sorted.
##Assume your inputs will be sufficient for the memory you have.
##Example inputs
##>>> 11,127,56,2,1,5,7,9,11,65,12,24,76,87,123,65,8,32,86,123,67,1,67,92,72,39,49,12
##>>> 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501


def check_if_sorted(details):
    """compares two consecutive integers in a list and returns the list if sorted else get the list sorted by calling another function"""
    i = 0
    while i <=  len(details) - 2:
        if details[i] < details[i+1]:
            status = True
            i = i+1
            print details
        else:
            bubble_sort(details)
    if status :
        return details
        

def bubble_sort(details):  
    """compares two consecutive integers in a list and shifts the smaller one to left """
    for i in range(len(details)-1):
        if details[i] > details[i+1]:
            temp = details[i]
            details[i]= details[i+1]
            details[i+1] = temp
    return check_if_sorted(details)
        
        
sort_me = [11,127,56,2,1,5,7,9,11,65,12,24,76,87,123,65,8,32,86,123,67,1,67,92,72,39,49,12, 98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,1501]
print sort_me 
print bubble_sort(sort_me)

            
        
                

