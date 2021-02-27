"""
Counter is a subclass of python dictionary and its primary purpose is to store values
and the `count` of those values.  Hashable elements are stored as the counter keys
and the count of them, as the value.  Retrieve a non existent value from a Counter
does not raise a `KeyError` but instead, it returns 0.

Assigning a Counters keys value to 0 does not remove it, the correct way to delete
a value from a counter instance is via the `del` keyword.

Counters function slightly differently in regards to both `fromkeys` & `update` 
respectively; This is outlined in the latter part of this document.
"""

# ------------------------------------------------------------------------------------------------

# Instantiating a Counter instance with an `Iterable`
def instantiate_iterable_counter():
  c = Counter("Hello World")  # Remember, strings are iterable :) 
  # Counter({'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
  
# Instantiating a Counter instance with a `Mapping`
def instantiate_mapping_counter():
  c = Counter({"a": 10, "b": 20, frozenset(["a,b"]): 1})  # Remember, frozensets are hashable :)
  # Counter({'a': 10, 'b': 20, frozenset({'a,b'}): 1})
  
# Instantiating a Counter instance with keyword args
def instantiate_kwargs_counter():
  c = Counter(a=1, b=2, c=3)
  # Counter({'a': 1, 'b': 2, 'c': 3})
  
# Getting non existing keys does not raise a KeyError; but instead returns 0
# Note: `.get()` still behaves exactly like a dict; thus defaulting to None!
def no_keyerror_on_bad_lookup():
  c = Counter(a=1, b=2, c=3)
  print(c['d'])  # 0
  print(type(c.get('f'))  # `NoneType`
  
# Deleting from the counter
def delete_from_counter():
  c = Counter("abc")
  c.subtract('a')
  # Counter({'a': 0, 'b': 1, 'c': 1})
  del c['a']
  # Counter({'b': 1, 'c': 1})
  
# ------------------------------------------------------------------------------------------------

"""
It is permitted, that Counter `count` values can be 0, or even negative.  In such circumstances
checking `elements()` on the instance of Counter, will ignore such values.  `elements()` is 
only one of the new functionality provided by the Counter subclass, all of them are:

  `c.elements()` returns an itertools.chain instance of keys for every 1 of their respective counts
  `c.most_common(n)` returns the `n` most common keys in the Counter.  if `n` is None or omitted, returns all.
  `c.subtract(iterable-or-mapping)
  
  -- `elements()`:  Element(s) returns an `itertools.chain` generator of each key, repeated for each count.
  In the event that a keys count is either negative, or 0 then `elements()` will not return any data for that 
  key.
  
  -- `most_common(n)`: Returns a list of Tuples `(Key, Count)` for the most popular counts, filterable via the
  n parameter.  By default if `n` is omitted or explicitly `None` then `most_common` will return tuples for
  all key/value pairs in the counter instance.  Negative counts, or counts of 0 are included in such groupings.
  
  -- `subtract(iterable_or_mapping)`: 
"""

# counter.elements()
def non_positive_counts_are_ignored_by_elements():
  c = Counter(a=0, b=-1, c=3)
  # Counter({'a': 0, 'b': -1, 'c': 3})
  print(list(c.elements()))  # ['c', 'c', 'c']
  
  
# counter.most_common(n)
def counter_most_common():
  c = Counter(a=1, b=2, c=3, d=4)
  print(c.most_common(1)) # [('d', 4)]
  c.most_common(None) == c.most_common()  # True
  print(c.most_common())  # [('d', 4), ('c', 3), ('b', 2), ('a', 1)]
  
  # negative or 0
  c = Counter(a=-1, b=0, c=1)
  print(c.most_common())  # [('c', 1), ('b', 0), ('a', -1)]
  
# counter.subtract(iterable_or_mapping)
def counter_subtract():
  ...
   
