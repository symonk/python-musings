# Python sets: The python set module provides classes for constructing and manipulating unordered groups of unique elements:

#  Sets do not allow duplicates
#  Sets are backed by hash tables and can not guarantee 'order', you should never rely on the order being correct



# <-- Notes on sets -->
this_is_actually_a_dictionary = {} # to instantiate an empty set, use set()
>>> type(empty_set_nope) -> <class 'dict'>


# Some of the main uses of using sets to solve problems are:
# Membership testing -> 1 in {1,2,3}
find_items = {1,2,3,4,5}
>>> 1 in find_items -> True
>>> 10 in find_items -> False

# Removing duplicates:
dupe_list = [1,1,2,3,4,4]
unique_items = set(dupe_list) >>> unique_items -> {1, 2, 3, 4}

# How to instantiate sets (see notes on using {} to instantiate an empty set!)
my_set = set() # Empty set -> type(my_set) -> <class 'set'>
my_other_set = {1,2,3,4,5} # set of len(5) -> <class 'set'>
comprehension_set = {x for x in range(1,10)}
>>> comprehension_set -> {1, 2, 3, 4, 5, 6, 7, 8, 9} >>> type(comprehension_set) -> <class 'set'>
set_from_iterable:
>>> set([1,2,3]) -> {1, 2, 3}
>>> set({'one': 1, 'two': 2}.keys()) -> {'one', 'two'}

# Set operations
# >>> Operation name: 'add()' | Args:




'add', 'clear', 'copy', 'difference', \
'difference_update', 'discard', 'intersection',\
'intersection_update', 'isdisjoint',
'issubset', 'issuperset', 'pop', 'remove',
'symmetric_difference', 'symmetric_difference_update',
'union', 'update']



# Performance of operations




# hashing again? equality?



# Making custom objects hashable for use?





# Fun facts, notes and things?
