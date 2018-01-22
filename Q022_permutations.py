###Problem : Given a list of strings, some of which may be anagrams amongst themselves, print the
###permutations which can be so constructed so that each permutation has set of strings which
###is completely unique.
###Example input:
###>>> “asda”, “daas”, “dand”, “nadd”
###{“asda”, “dand”}, {“daas”, “dand”}, {“asda”, “nadd”}, {“daas”, “nadd”},
###>>> “laptop”, “toplap”, “loptap”, “mouse”
###{“laptop”, “mouse”}, {“toplap”, “mouse”}, {“loptap”, “mouse”}
def anagram(value):
    '''Prints random anagram of given value'''
    import random
    newWord = ''
    for i in range(len(value)):
        pos = random.randint(0, len(value)-1)
        newWord += value[pos]
        value = value[:pos] + value[pos+1:]
    return newWord

def random_set(input_value):
    if len(input_value) <= 2:
        output = input_value
    else:
        for i in range(len(input_value) - 1):
            for j in range(1,len(input_value) - 1):
                print i , j
                print anagram(input_value[j])
                if input_value[i] != anagram(input_value[j]):
                    output = {input_value[i] ,input_value[j]}


    return output
    
print random_set(["asda", "daas" , "dand" , "naad"])

