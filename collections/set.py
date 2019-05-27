# Python sets: The python set module provides classes for constructing and manipulating unordered groups of unique elements:

#  Sets do not allow duplicates
#  Sets are backed by hash tables and can not guarantee 'order', you should never rely on the order being correct



# <-- Notes on sets -->
this_is_actually_a_dictionary = {} # to instantiate an empty set, use set()
>>> type(empty_set_nope) ---> <class 'dict'>

# Sets can only hold hashable objects, trying to add a list to a set will not work as list is not hashable for example
# Sets by default in python 3 take up 224 bytes when empty
# Sets are extremely memory hungry, in comparison to lists:
>>> getsizeof(set(range(100)))
8416
>>> getsizeof(range(100))
48
>>>

# __slots__ can be implemented as a means to help with shrinking memory usage

# Some of the main uses of using sets to solve problems are:
# Membership testing -> 1 in {1,2,3}
find_items = {1,2,3,4,5}
>>> 1 in find_items --> True
>>> 10 in find_items --> False

# Removing duplicates:
dupe_list = [1,1,2,3,4,4]
unique_items = set(dupe_list) >>> unique_items --> {1, 2, 3, 4}

# How to instantiate sets (see notes on using {} to instantiate an empty set!)
my_set = set() # Empty set -> type(my_set) -> <class 'set'>
my_other_set = {1,2,3,4,5} # set of len(5) -> <class 'set'>
comprehension_set = {x for x in range(1,10)}
>>> comprehension_set -- {1, 2, 3, 4, 5, 6, 7, 8, 9} >>> type(comprehension_set) --> <class 'set'>
set_from_iterable:
>>> set([1,2,3]) -> {1, 2, 3}
>>> set({'one': 1, 'two': 2}.keys()) -> {'one', 'two'}

# Set operations
# >>> Operation name: 'add()' | Args: 'element' to be added to the set (must be hashable!)
# What do we mean by hashable? for custom objects you should implement dunder __eq__ & __hash__
test_set = set().add(5)
test_set = set().add((1,2,3,4,5)) # Adding a tuple of values (hashable, iterable)

# >>> Operation name: 'clear' | Args: none
# Completely empties the set


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
