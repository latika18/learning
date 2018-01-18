

def merge_sort(list_sort):
    """splits the list in two parts until each part is left with one member"""

    if len(list_sort) ==  1:
        return list_sort
   
    if len(list_sort)>= 2:
        x= len(list_sort) / 2
        part_a = list_sort[:x]
        part_b = list_sort[x:]
        sorted_part_a = merge_sort(part_a)
        sorted_part_b = merge_sort(part_b)
        return merge(sorted_part_a, sorted_part_b)
    
            
def merge(left , right):
    """merges the two parts of list after sorting them"""
    sorted_list = []
    i = 0
    while left[:] and right[:] :
        if  left [i] > right [i]:
            sorted_list.append(right[i])
            right.remove(right[i])
            
        else :
            sorted_list.append(left[i])
            left.remove(left[i])
            
    if left[:]:
            sorted_list.extend(left[:])
    elif right[:] :
            sorted_list.extend(right[:])
    return sorted_list

details = [1,127,56,2,1,5,7,9,11,65,12,24,76,87,123,65,8,32,86,123,67,1,67,92,72,39,49,12 ,98,52,45,19,37,22,1,66,943,415,21,785,12,698,26,36,18,97,0,63,25,85,24,94,150]
print "List to be sorted  = ", details
print "Sorted List = ", merge_sort(details)


