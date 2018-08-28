def unique(string1):
    status = True
    for i, v in enumerate(string1):
        if v not in string1:
            status = True
        else:
            status = False
        string1 = string1[i:]
        
    return status
