##Write a method to decide if two strings are anagrams or not

def is_anagram(wd1,wd2):
    for c in wd1:
        wd1= wd1.replace(c,"")
        while wd1:
            if c in wd2:
                wd2 = wd2.replace(c, "")
                print c , wd1, wd2
            else:
                return False
    print len(wd2)
    if len(wd2)== 0:
        return True
    else:
        return False


print is_anagram('xxrrrxx','xxx')
    


