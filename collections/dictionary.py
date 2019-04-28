#  Find here some interesting facts and learning material on the python dictionary

# Python dictionaries are collection(s) that are backed by a hash table (with build in collision algorithms) if you are
# familiar with the likes of java, they are your hash map -> a hash table backed collection of key value pairs

 # Note 1: Dictionaries are 'mutable' so you need not know all entries in advance
 # Note 2: As of python 3.7 dictionaries maintain their insertion order
 # Note 3: Dictionaries hold an internal size of '8' on instantiation
 # Note 4: Dictionaries acquire 240 bytes in memory (8 slots) on instantiation of an empty dict
 # Note 5: Dictionaries auto-resize when they are two-thirds full, 66% auto resizing occurs
 # Note 6: Shrinking dictionaries with 'del' will not make the dict smaller, dummy keys must be kept in memory to resolve hash collisions
 # Note 7: Dictionaries are heterogenerous, you can store anything you like (minus a few caveats)
 # Note 8: Dictionaries keys MUST be unique, duplicate value(s) is acceptable
 # Note 9: Dictionary keys must be immutable (if the hash of the key changes, the dictionary would be screwed)
 # Note 10: To use custom object types as dictionary keys, they should implement both __eq__ and __hash__ (__ne__ too if you want)

-------------------------------------------------------------------------------------------------------------
# Instantiation:
empty_dict_a = dict() # empty dict
empty_dict_b = {} # empty dict
dict_c = {'a': 'A', 'b': 'B'} # dict of length 2, passing in literal values
dict_from_tuples = {[("Hello" , 7), ("hi" , 10), ("there" , 45),("at" , 23),("this" , 77)]} # dict of len 5
dict_from_only_keys = dict.fromkeys(['one', 'two', 'three'], 'default') # dict of len 3 (all values 'default')
dict_from_zipped_lists = dict(zip(['a', 'b', 'c'], [1,2,3])) # dict of len 3, from 2x zipped lists

-------------------------------------------------------------------------------------------------------------

# Operations
the_dict = {}

the_dict.clear() # completely empties the dictionary, leaving an empty dictionary:
the_dict.copy() # creates a 'shallow' copy of the items, by shallow copy we mean the contents of the dictionary is not copied by value, instead just creating a new reference
the_dict.fromkeys() # creates a new dictionary from a sequence of 'keys', value= can be set to override the default of None
the_dict.get() # retrieve an item from the dictionary, returns None if the key is not found, so no KeyError raised, supports a default value
the_dict.items() # returns an instance of dict_items which

-------------------------------------------------------------------------------------------------------------

# Operations in action
dict.clear():

dict.copy():

dict.fromkeys():

```python
>>> a = dict.fromkeys(list)
>>> a
{1: None, 2: None, 3: None, 4: None, 5: None}
>>> a = dict.fromkeys(list, 1337)
>>> a
{1: 1337, 2: 1337, 3: 1337, 4: 1337, 5: 1337}
```

dict.get():

```python
>>> d = dict(zip(range(1,10), range(1,10)))
>>> d
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
>>> d.get(10) # returns None
>>> d.get('a') # returns None
>>> d.get(10, 'Default')
'Default'
```


-------------------------------------------------------------------------------------------------------------

# Operations in terms of Big-O:


-------------------------------------------------------------------------------------------------------------

# Dictionary Comprehensions




-------------------------------------------------------------------------------------------------------------

# Various flavours of dictionaries

# orderedDict, chained etc


-------------------------------------------------------------------------------------------------------------
