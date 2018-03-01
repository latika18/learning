# -*- coding: cp1252 -*-
##Given a list of strings, some of which may be anagrams amongst themselves, print the
##permutations which can be so constructed so that each permutation has set of strings which is completely unique.
##Example input:
##>>> “asda”, “daas”, “dand”, “nadd”
##{“asda”, “dand”}, {“daas”, “dand”}, {“asda”, “nadd”}, {“daas”, “nadd”},
##>>> “laptop”, “toplap”, “loptap”, “mouse”
##{“laptop”, “mouse”}, {“toplap”, “mouse”}, {“loptap”, “mouse”}


def is_anagram(value_1, value_2):
    """checks whether the two given strings are anagrams """
    if sorted(value_1) == sorted(value_2):
        return True
        
def random_set(input_value):
    """returns the set of strings which are completely unique"""
    if len(input_value) <= 2:
        output = input_value
    else:
        output = []
        for i in range(len(input_value)):
            for j in range(len(input_value)):
                if not is_anagram(input_value[i], input_value[j]):
                    output.append( {input_value[i], input_value[j]})

    return output

print random_set(["asda", "daas" , "dand" , "nadd"])
print random_set(["laptop", "toplap", "loptap", "mouse"])




