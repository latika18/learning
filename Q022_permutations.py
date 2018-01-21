Given a list of strings, some of which may be anagrams amongst themselves, print the
permutations which can be so constructed so that each permutation has set of strings which
is completely unique.
Example input:
>>> “asda”, “daas”, “dand”, “nadd”
{“asda”, “dand”}, {“daas”, “dand”}, {“asda”, “nadd”}, {“daas”, “nadd”},
>>> “laptop”, “toplap”, “loptap”, “mouse”
{“laptop”, “mouse”}, {“toplap”, “mouse”}, {“loptap”, “mouse”}
