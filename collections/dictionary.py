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

-------------------------------------------------------------------------------------------------------------

# Operations
the_dict = {}

the_dict.clear() # completely empties the dictionary, leaving an empty dictionary:
the_dict.copy() # creates a 'shallow' copy of the items, by shallow copy we mean the contents of the dictionary is not copied by value, instead just creating a new reference
the_dict.fromkeys() # creates a new dictionary from a sequence of 'keys', value= can be set to override the default of None

```python
>>> a = dict.fromkeys(list)
>>> a
{1: None, 2: None, 3: None, 4: None, 5: None}
>>> a = dict.fromkeys(list, 1337)
>>> a
{1: 1337, 2: 1337, 3: 1337, 4: 1337, 5: 1337}
```


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
