# Question : Create a function that given a string, prints a random anagram of it
#defining the function anagram
def anagram(value):
    import random
    print len(value)
    newWord = ''
    for i in range(len(value)):
        pos = random.randint(0,len(value)-1)
        newWord += value[pos]
        value = value[:pos] + value[pos+1:]
        
    print newWord
anagram('tanush')
anagram('  ')


    
