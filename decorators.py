#  Find here some interesting facts and learning material on the python dictionary

# Python dictionaries are collection(s) that are backed by a hash table (with build in collision algorithms) if you are
# familiar with the likes of java, they are your hash map -> a hash table backed collection of key value pairs


# dictionaries are 'mutable' so you need not know all entries in advance (unlike tuples)
-------------------------------------------------------------------------------------------------------------
# Instantiation:
empty_dict_a = dict() # empty dict
empty_dict_b = {} # empty dict
dict_c = {'a': 'A', 'b': 'B'} # dict of length 2, passing in literal values
dict_from_tuples = {[("Hello" , 7), ("hi" , 10), ("there" , 45),("at" , 23),("this" , 77)]} # dict of len 5
dict_from_only_keys = dict.fromkeys(['one', 'two', 'three'], 'default') # dict of len 3 (all values 'default')
dict_from_zipped_lists = dict(zip(['a', 'b', 'c'], [1,2,3])) # dict of len 3, from 2x zipped lists
