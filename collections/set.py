"""
Python offers two flavours of built in sets, these are sets and frozen sets.
As you can imagine, frozen sets are themselves immutable and thus hashable so can be stored inside other sets
and also used as dictionary keys.  By default, sets are mutable as we can add elements to them etc.

Note: For TLDR Notes, please reference the end of this file.
"""

# Demonstration of mutability, hashability and frozen sets as hashable keys / set elements

mutable_set = {1, 2, 3, 4}
immutable_set = frozenset([1, 2, 3, 4])

empty_set = set()
empty_set.add(mutable_set)
"""
Traceback (most recent call last):
  File "C:/workspace/learning-python/collections/set.py", line 13, in <module>
    empty_set.add(mutable_set)
TypeError: unhashable type: 'set'
"""

empty_set.add(immutable_set)
# {frozenset({1, 2, 3, 4})}

# Adding as dictionary keys:
"""
>>> mydict = {mutable_set: 'mutable!'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
"""

# Vs frozen:

"""
>>> mydict = {immutable_set: 'immutable!'}
>>> mydict
{frozenset({1, 2, 3, 4}): 'immutable!'}
"""

------------------------------------------------------------------------------

"""
A set by definition (Set Theory) is an unordered collection of distinct, hashable elements.
The core benefits of sets in python are:
 - Extremely fast 'in' checks, 'x' in {'x', 'y', 'z'} for example
 - Remove duplicates from other collections
 - Applying various mathematically operations, such as union & intersection etc.
 
Sets out of the box support len(set), for x in set:, x in set.  Notably, sets are NOT sequences so index lookup,
slice notation and other sequence like behaviour.  Importantly sets cannot guarantee the order of elements.  Sets do 
not keep track of order of insertion, or current order of elements.  Instead they use the hash of elements to compute
where the object A) should be placed and B) should be retrieved from extremely fast. 

"""

------------------------------------------------------------------------------

"""
Sets can be constructed through two main methods, firstly using the curly braces:

>>> my_set = {1,2,3,4}
>>> type(my_set)
<class 'set'>

>>> my_set = set([1,2,3,4])
>>> type(my_set)
<class 'set'>

The core difference in these two approaches is that using the set constructor approach explicitly (set(iterable))
only accepts a single, (optional) iterable item, whereas with the braces approach, all items should be explicitly
passed in.  Note: A set CANNOT hold references to A) dictionaries and B) Lists because those two types are non hashable
due to their mutable nature.  This is shown below:

>>> my_dict = dict(a=1, b=2, c=3)
>>> new_set = {my_dict}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

>>> my_list = [_ for _ in range(100)]
>>> my_set = set()
>>> my_set.add(my_list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

Note: Lists are an iterable, as are dictionaries (by default on keys) so this approach works just fine:

>>> immutable_list = [_ for _ in range(5)]
>>> immutable_dict = {'a': 1, 'b': 2}
>>> my_set = set(immutable_list)
>>> my_set
{0, 1, 2, 3, 4}
>>> my_set = set(immutable_dict)
>>> my_set
{'a', 'b'}

As you an see above, both of these mutable types are infact, iterables so they can be unpacked into the set.

"""

------------------------------------------------------------------------------

"""
By default as of python 3.8.5, sets are 216 bytes in size when empty.
This applies to both sets and frozen sets

>>> get_size(set())
216
>>> get_size(frozenset())
216
"""

------------------------------------------------------------------------------

"""
Python set methods are outlined below:

['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', 
'__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', 
'__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', 
'__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', 
'__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 
'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union', 'update']

"""


------------------------------------------------------------------------------

"""
TLDR Notes:
# Two types of built in set (set() / frozenset())
# Create sets using set(iterable), frozenset(iterable), {n,...}
# By default, empty braces will create a dictionary (care) = {} # Type Dict, not an empty set!
# By default, python sets are allocated sizing for 8 elements. 
# By default, resizing occurs when the set is 60%~ (TODO FIX THIS) full? seems to resize 3.5x its size?
"""