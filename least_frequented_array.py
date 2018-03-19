#Python 3 program to find the least
# frequent element in an array.
 
 
def leastFrequent(arr, n) :
 
    # Sort the array
    arr.sort()
  
    # find the min frequency using
    # linear traversal
    min_count = n + 1
    res = -1
    current_count = 1
    for i in range(1, n) :
        if (arr[i] == arr[i - 1]) :
            current_count = current_count + 1
        else :
            if (current_count < min_count) :
                min_count = current_count
                res = arr[i - 1]
             
            current_count = 1
             
   
    # If last element is least frequent
    if (current_count < min_count) :
        min_count = current_count
        res = arr[n - 1]
     
    return res
     
  
# Driver program
arr = [1, 3, 2, 1, 2, 2, 3, 1]
n = len(arr)
print(leastFrequent(arr, n))
 
 
