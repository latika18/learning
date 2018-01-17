

def merge_sort(list_sort):
    """splits the list in two parts until each part is left with one member"""

    if len(list_sort) ==  1:
        print len(list_sort)
        return list_sort
   
    if len(list_sort)>= 2:
        x= len(list_sort) / 2
        part_a = list_sort[:x]
        part_b = list_sort[x:]
        print part_a , part_b
        sorted_part_a = merge_sort(part_a)
        sorted_part_b = merge_sort(part_b)
        return merge(sorted_part_a, sorted_part_b)
    
            
def merge(left , right):
    """merges the two parts of list after sorting them"""
    print left, right 
    sorted_list = []
    i , j = 0
    if len(left) >= len(right):
        i = len(left)
        while i != 0:
            if left[i] > right[i]:
                sorted_list.append(right[i])
            else :
                sorted_list.append(left[i])
            i = i-1
        sorted_list += right[i:]
    else :
        i = len(right)
        while i != 0:
            if left[i] > right[i]:
                sorted_list.append(right[i])
            else :
                sorted_list.append(left[i])
            i = i-1
        sorted_list += left[i:]
    return sorted_list

details = [3, 7, 5, 12, 14, 11, 2, 6]
print merge_sort(details)


