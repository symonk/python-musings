#  Find here some interesting facts and learning material on the python dictionary

# Python dictionaries are collection(s) that are backed by a hash table (with built in collision algorithms) if you are
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
 # Note 11: Dictionaries can be nested, as in contain dictionaries of dictionaries of dictionaries, not keys of course, dicts aren't hashable!
 # Note 12: In Python 3 Dict: .items(), .keys(), .values() returns 'View' Object that we can iterative over, to avoid building a list to iterate on for better efficiency
 # Note 13: .clear() sets the dict size to 72 bytes (not 240) as it re-wired to a statically allocated empty key-space (C-code)
 # Note 14: .popitem() as of python 3.7 is now guaranteed LIFO removal as the insertion order is guaranteed as per Note: 2
 # Note 15: .update() performs an in-place update, returning None (just like list appending etc)
 # Note 16: .update() overrides existing keys with the newer value, non existent keys will be added
 # Note 17: dict **kwargs instantiation is only viable when the keys are simple strings
 # Note 18: Dictionary views (keys, items, values) are a 'window' into the dict and reflect any change(s) in real time. they are iterable and do not build lists when iterating
 # Note 19: Even with python3 view efficiency changes, `x in dict` is king for checking if a key exists in a dictionary
 # Note 20: Always favour {} over dict() unless {} does not fit your use case, performance gains (while minor) can be had

-------------------------------------------------------------------------------------------------------------
# Instantiation:
empty_dict_a = dict() # empty dict
empty_dict_b = {} # empty dict
dict_c = {'a': 'A', 'b': 'B'} # dict of length 2, passing in literal values
dict_from_tuples = {[("Hello" , 7), ("hi" , 10), ("there" , 45),("at" , 23),("this" , 77)]} # dict of len 5
dict_from_only_keys = dict.fromkeys(['one', 'two', 'three'], 'default') # dict of len 3 (all values 'default')
dict_from_zipped_lists = dict(zip(['a', 'b', 'c'], [1,2,3])) # dict of len 3, from 2x zipped lists
dict_simple_strings = dict(one=1, two=2)

-------------------------------------------------------------------------------------------------------------
# Operations
the_dict = {}

the_dict.clear() # completely empties the dictionary, leaving an empty dictionary:
the_dict.copy() # creates a 'shallow' copy of the items, by shallow copy we mean the contents of the dictionary is not copied by value, instead just creating a new reference
the_dict.fromkeys() # creates a new dictionary from a sequence of 'keys', value= can be set to override the default of None
the_dict.get() # retrieve an item from the dictionary, returns None if the key is not found, so no KeyError raised, supports a default value
the_dict.items() # returns an instance of dict_items (Dynamic View) which
the_dict.keys() # returns an instance of dict_keys (Dynamic View) which
the_dict.values() # returns an instance of dict_values (Dynamic View) which
the_dict.pop() # removes the specified key in the dictionary and returns its value.  Raises a KeyError on non existent key, unless default is provided
the_dict.popitem() # removes the last entry of a dict, returning its key and value pair in a tuple, returns KeyError if dict is empty
the_dict.setdefault() # insert a key with value of default= if the key does not exist, else return the value for the key if it exists (else default)
the_dict.update() # performs an in-place update to the dict (@caveat: returns None), update expects an iterable of: k:v pairs, another dict or **kwargs (non existent keys are added)
-------------------------------------------------------------------------------------------------------------
# Operations in action
dict.clear():

```python
    >>> d = {1:1, 2:2, 3:3}
    >>> d
    {1: 1, 2: 2, 3: 3}
    >>> d.clear()
    >>> d
    {}
```

---

dict.copy():

```python
    >>> d = {1:1, 2:2, 3:3}
    >>> d1 = d.copy()
    >>> d
    {1: 1, 2: 2, 3: 3}
    >>> d1
    {1: 1, 2: 2, 3: 3}
```

---

dict.fromkeys():

```python
    >>> a = dict.fromkeys(list)
    >>> a
    {1: None, 2: None, 3: None, 4: None, 5: None}
    >>> a = dict.fromkeys(list, 1337)
    >>> a
    {1: 1337, 2: 1337, 3: 1337, 4: 1337, 5: 1337}
```

---

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

dict.keys() && dict.values() && dict.items():

```python
    >>> d = {1:1, 2:2, 3:3}
    >>> d.items()
    dict_items([(1, 1), (2, 2), (3, 3)])
    >>> d.keys()
    dict_keys([1, 2, 3])
    >>> d.values()
    dict_values([1, 2, 3])
```

---

dict.pop():

```python
    >>> d = {'pop': 1, 'pop2': 2}
    >>> d.pop('pop2')
    2
    >>> d
    {'pop': 1}
    >>> d.pop('popper', 'def')
    'def'
    >>> d.pop('key-error')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'key-error'
```

---

dict.popitem():

```python
    >>> d = {'one': 1}
    >>> d.popitem()
    ('one', 1)
    >>> d.popitem()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'popitem(): dictionary is empty'
```

---

dict.setdefault():

```python
    >>> d = {1:1, 2:2, 3:3}
    >>> d.setdefault(4, 'default')
    'default'
    >>> d
    {1: 1, 2: 2, 3: 3, 4: 'default'}
    >>> d.setdefault(3, 'default') # 3 exists so lets get '3'
    3
    >>> d
    {1: 1, 2: 2, 3: 3, 4: 'default'}
```

---

dict.update():

```python
    >>> upd8_dict = dict(one=1, two=2, three=3)
    >>> upd8_dict.update(dict(two=20, four=4))
    >>> upd8_dict
    {'one': 1, 'two': 20, 'three': 3, 'four': 4}

    >>> upd8_kwargs = dict(one=1, two=2, three=3)
    >>> upd8_kwargs.update(dict(two=20, four=4))
    >>> upd8_kwargs
    {'one': 1, 'two': 20, 'three': 3, 'four': 4}

    >>> keyvalue = {1: 100, 2: 200, 3: 300}
    >>> keyvalue.update([(1, 1000), (2, 2000), (3, 3000)])
    >>> keyvalue
    {1: 1000, 2: 2000, 3: 3000}
```

-------------------------------------------------------------------------------------------------------------
# Operations in terms of Big-O:
# Dictionaries, backed by hash tables are extremely efficient for updating, inserting
big_o_dict = {}

| Operation   | Average Case | Worst Case |
|-------------|--------------|------------|
| Copy        | O(N)         | O(N)       |
| Get         | O(1)         | O(N)       |
| Set         | O(1)         | O(N)       |
| Delete      | O(1)         | O(N)       |
| Instantiate | O(N)         | O(N)       |

-------------------------------------------------------------------------------------------------------------
# Dictionary Comprehensions
# Python itself offers a number of 'comprehensions' for collections, for example list comprehensions also exist
# Typical syntax for dict comprehensions is: {key:value FOR key, value IN (iterable) IF (boolean expression(s))

list_of_colours = ['red', 'blue', 'green']
set_of_numbers = {1,2,3}
dict_comp = {key:value for key, value in zip(list_of_colours, set_of_numbers)}

```python
    >>> list_of_colours = ['red', 'blue', 'green']
    >>> set_of_numbers = {1,2,3}
    >>> dict = {key:value for key, value in zip(colours, numbers)}
    >>> dict
    {'red': 1, 'blue': 2, 'green': 3}
    >>>
```python

# more examples:
dict_comp = {key: key * 10 for key in range(0, 100)}

```python
>>> dict_comp = {key: key * 10 for key in range(0, 100)}
>>> dict_comp
    {0: 0, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100, 1
    1: 110, 12: 120, 13: 130, 14: 140, 15: 150, 16: 160, 17: 170, 18: 180, 19: 190,
    20: 200, 21: 210, 22: 220, 23: 230, 24: 240, 25: 250, 26: 260, 27: 270, 28: 280,
     29: 290, 30: 300, 31: 310, 32: 320, 33: 330, 34: 340, 35: 350, 36: 360, 37: 370
    , 38: 380, 39: 390, 40: 400, 41: 410, 42: 420, 43: 430, 44: 440, 45: 450, 46: 46
    0, 47: 470, 48: 480, 49: 490, 50: 500, 51: 510, 52: 520, 53: 530, 54: 540, 55: 5
    50, 56: 560, 57: 570, 58: 580, 59: 590, 60: 600, 61: 610, 62: 620, 63: 630, 64:
    640, 65: 650, 66: 660, 67: 670, 68: 680, 69: 690, 70: 700, 71: 710, 72: 720, 73:
     730, 74: 740, 75: 750, 76: 760, 77: 770, 78: 780, 79: 790, 80: 800, 81: 810, 82
    : 820, 83: 830, 84: 840, 85: 850, 86: 860, 87: 870, 88: 880, 89: 890, 90: 900, 9
    1: 910, 92: 920, 93: 930, 94: 940, 95: 950, 96: 960, 97: 970, 98: 980, 99: 990}
    >>>
```

-------------------------------------------------------------------------------------------------------------
# Various flavours of dictionaries

# orderedDict, chained etc

-------------------------------------------------------------------------------------------------------------
# Simple problems with dictionaries, with solutions

-------------------------------------------------------------------------------------------------------------
# More on hashing, how it works and the collision algorithm explained

-------------------------------------------------------------------------------------------------------------
