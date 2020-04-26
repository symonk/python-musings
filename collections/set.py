# Python sets: A collection used to store hashable unique elements.  Ordering is not guaranteed here and in order
# to store an element in a set, it must be hashable.  Custom objects should implement both a __eq__ and __hash__ in
# order to qualify for storage.

# Creating a new set, note: instantiating an empty set should be used directly by creating an instance below:
my_set = set()
set_with_elements = {1,2,3,4,5}

# Why? because using braces to instantiate an empty set will actually give you a <class 'dict'> type
not_a_set = {} # syntactically looks OK, the outcome - maybe surprising
"""
>>> type(not_a_set)
<class 'dict'>
"""

# sets by default as of python consume a total of 224 bytes of memory.
"""
>>> from sys import getsizeof as size
>>> size(set())
224
"""

# Sets as previously mentioned can only store hashable objects, as a result adding a list into a set is not permitted.
# Previously when storing a set inside another set, python did some magic and auto converted the set to an ImmutableSet.
# This is no longer the case, and frozenset() is the preferred way to do things now, this should be done manually. In
# order to add custom objects into a set the users custom instances must have an overridden __eq__ and __hash__.  All
# of this information is outlined below.  Note: sets are pretty memory hungry, especially compared to lists!

# Storing a non hashable type in a set:
"""
>>> list_in_set = {[1,2,3]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
"""

# No longer auto converting sets in sets to ImmutableSet:

"""
>>> two = {one}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
"""

# The solution, use a frozenset()

"""
>>> one = frozenset([1,2,3])
>>> two = {one}
>>> for item in two: print(type(item))
...
<class 'frozenset'>
"""

# Default custom class (by default by actually do have a __eq__ and __hash__ implementation, however it will say that
# by default; all instances of such class are UNIQUE regardless.  In order to have them correctly (I say correctly as
# if you see below, a default dummy class can be added to a set multiple times) we should implement __eq__ and __hash__
# Lets take a look below:

"""
>>> class Dummy:
...     pass
...
>>>
>>>
>>> one = set()
>>> one.add(Dummy())
>>> one.add(Dummy())
>>> one
{<__main__.Dummy object at 0x00000161C4A6F710>, <__main__.Dummy object at 0x00000161C4A6F668>}
"""
# The above is surprising, set accepts both instances as unique (non duplicate) elements, But is __eq__ on its own enough?

"""
>>> class DummyTwo:
...     def __init__(self):
...             self.x = 10
...     def __eq__(self, other):
...             return self.x == other.x
...
>>>
>>> one = set()
>>> one.add(DummyTwo())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'DummyTwo'
>>>
"""

# Wait a minute, this is even worse - we added only a __eq__ implementation into our new class, and now the set just
# straight up blocks us, what python is going on under the hood?  By default when we have the initial Dummy class, python
# automatically applies the __eq__ and __hash__ for us (albeit a very lackluster one) in terms of true equality.  By
# implementing the __eq__ method, python has automatically removed the __hash__ method from our object? when a custom
# instance has an overriden __eq__ than that of object, the __hash__ implement returns None.

"""
>>> class Hashable:
...     def __init__(self, value):
...             self.value = value
...
...     def __eq__(self, other):
...             return self.value == other.value
...
...     def __hash__(self):
...             return hash(self.value)  # for demo purposes; do something better than this!

>>> one = Hashable(10)
>>> two = Hashable(20)
>>> three = Hashable(10)
>>> one == three
True
>>> my_set = {one, three}
>>> my_set
{<__main__.Hashable object at 0x00000161C4A734A8>}

"""

# As shown above, one and three are now considered equally, and correctly handled by the set collection.  Just to touch
# on the previous point about the __eq__ override without __hash__, this is bad practice and you should avoid doing this.
# if you have the need to override __eq__ ALWAYS override __hash__ too.  Lets see the value from __hash__ when only
# __eq__ is implemented:

"""
>>> class EqOnlyNoHash:
...     def __eq__(self, other):
...             # return True always the same!
...             return True
...
>>> one = EqOnlyNoHash()
>>> two = EqOnlyNoHash()
>>> one == two
True
>>> hash_val = hash(one)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'EqOnlyNoHash'
"""

# As we can see, equality checks still work; but hashing is not supported! and a TypeError is raised by python.

# ---------------------------------------------------------------------------------------------------------------

# Some of the core uses of sets in python and when you should tend to use them are:
    # Removing duplicates from a group of elements
    # Requiring fast membership testing (in / not in)


# No Duplication: Sets are great at removing duplicate(s), since we have touched on eq/hash now, we understand what
# actually makes objects 'duplicates' as far as custom object instances go.  Lets see how we can use python sets to
# remove duplicate data from hashable type(s).

"""
>>> class Custom:
...     def __init__(self, val):
...             self.val = val
...
...     def __eq__(self, other):
...             return self.val == other.val
...
...     def __hash__(self):
...             return hash(self.val)

>>> one = Custom(val=10)
>>> two = Custom(val=10)
>>> mylist = [one, two]
>>> myset = set(mylist) # set from an iterable (list in this instance)
>>> myset
{<__main__.Custom object at 0x000001B0FD11FAC8>}

"""

#  As we can see above, due to eq/hash checks python determines one and two as identicle objects and thus the set only
# has a copy of one of them, if you are wondering - but which one, does the last one override the first one? we can
# easily check this using the builtin id() function:
# note: membership checks will return True for both instances here; after all you have decided they are equivalently the
# same object!

"""
>>> id(one)
1859671685832
>>> id(two)
1859671700144

But how do we get a single element from the set? convert it to a tuple or so, for this we will use max as we know it
only has 1 element, but interesting what would you expect the id() to return? it seems in reality python does not override
the duplicate value that was passed in, instead it retains the original:

>>> id(one)
1859671685832
>>> id(two)
1859671700144
>>> id(max(myset))
1859671685832 # this is the pointer to variable 'one'
"""

# So membership testing is quick, we know this - but how quick is it? Lets experiment (with a custom object):

"""
>>> class Performant:
...     def __init__(self, value):
...             self.value = value
...     def __eq__(self, other):
...             return self.value == other.value
...     def __hash__(self):
...             return hash(self.value)
...

>>> to_find = Performant(value=250)
>>> biglist = [Performant(value=x) for x in range(250000)]
>>> timeit(lambda: to_find in biglist, number=1000)
0.031744500000058906
>>> bigset = {Performant(x) for x in range(250000)}
>>> timeit(lambda: to_find in bigset, number=1000)
0.00036150000005363836
"""

# As we can see from the above, finding a particular element in a set is much faster than a list, but lets look at
# one of the common downsides; memory usage:

"""
>>> size(biglist)
2115952
>>> size(bigset)
8388832
"""

# the big list is using just slightly over 2 megabytes in memory; however the set is using nearly 4x.
# list: 2.1 MB
# set: 8.3 MB

# ---------------------------------------------------------------------------------------------------------------

# Now lets have a look at the capabilities of the set class, to see its bespoke methods, we can parse them out by
# excluding all the dunder methods for now, these are outlined below, n.b dir() returns alphabetically sorted list of
# the attributes, so these are already in alphabetical order, and we will discuss them in exactly that order.

"""
>>> myset = set()
>>> names = [x for x in dir(myset) if '__' not in x]
>>> names
['add', 
'clear', 
'copy', 
'difference', 
'difference_update', 
'discard', 
'intersection', 
'intersection_update', 
'isdisjoint', 
'issubset', 
'issuperset', 
'pop', 
'remove', 
'symmetric_difference', 
'symmetric_difference_update', 
'union', 
'update']
"""

# >>> Operation name: 'add' | Args:
# >>> Description:
# >>> Big O Notation of such operation:
# >>> Example python code below:




# printing of sets
# set comprehensions
# how does the backing hashing mechanism work
# set resizing etc
# tips and tricks on sets
