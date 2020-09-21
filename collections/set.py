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
Python set methods [excluding dunder / private]:

>>> pprint(set_interface)
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


"""
set add(elem) function:
 - Add a new (hashable, immutable) element to the set
 - Elements cannot be added at a particular index and the set has no record of where elements are
 - If the element already exists, nothing happens
 -- args: elem (the element to be added, if element already exists nothing happens)
 -- returns: None
 -- Big O: adding to a python set is O(1) constant. note: it is possible to hit collisions (multiple) times making a 
 -- completely worst case o(n).

"""

"""
set clear() function:
 - Remove all elements from the set
 - This resizes the set accordingly as outlined below:
 
     >>> x = set([_ for _ in range(100)])
    >>> get_size(x)
    8408
    >>> x.clear()
    >>> get_size(x)
    216

-- Big O: Clearing the set is a constant operation at: O(1). similar to x = set()
 
"""


"""
set copy() function:
 - Creates a shallow copy of the set (not a deep copy!)
    >>> one = set([1,2,3,5,6,7])
    >>> two = one.copy()
    >>> from sys import getrefcount
    >>> getrefcount(one)
    2
    >>> getrefcount(two)
    2
    >>> one.add(8)
    >>> two
    {1, 2, 3, 5, 6, 7}
    >>> # vs the assignment approach
    >>>
    >>> one = set([1,2,3,4,5,6,7])
    >>> two = one
    >>> getrefcount(one)
    3
    >>> getrefcount(two)
    3
    >>> # see the same references ^
    >>> one.add(8)
    >>> one
    {1, 2, 3, 4, 5, 6, 7, 8}
    >>> # two will also have 8
    >>> two
    {1, 2, 3, 4, 5, 6, 7, 8}
    
    >>> class ShallowCopy:
...     def __init__(self, x: int) -> None:
...             self.x = x
...
    >>> one = ShallowCopy(100)
    >>> var = {one}
    >>> var2 = var.copy()
    >>> for x in var:
    ...     print(id(x))
    ...
    1623954326816
    >>> for x in var2:))
    ...     print(id(x))
    ...
    1623954326816
    
    -- Big O Notation: Due to having to iterate the set to copy, copy() is O(N), linear

"""

"""
set difference(*others) function:
set x - y function:
 - The difference() function, also implemented through the __sub__ / __rsub__ dunder method of sets returns a new
 - set with the different items from set X which do not appear in others.  This is outlined below:

 # difference() can be called without argument and in this instance, will return the set of x:
    >>> x = set([1,2,3,4,5,6])
    >>> x.difference()
    {1, 2, 3, 4, 5, 6}
    # note this is equal to x.difference(set())

    >>> other_x = set([1,3,5,7,9])
    >>> other_y = set([2,4,6,8,10])
    >>> x - other_x
    {2, 4, 6}
    >>> x - other_y
    {1, 3, 5}

    # Applying difference to multiple *others:
    >>> x = {1,2,3,4,5,6,7,8,9,10,1337}
    >>> x.difference(other_x, other_y)
    {1337}

    # Same as:
    >>> x - other_x - other_y
    {1337}

    -- Big O Notation: x.difference(y) is equivalent to O(len(x) - len(y))

"""

"""
set difference_update(*others) function:
 - Update set X to remove items in *others. 
 - note: This updates X and does not create a new set
 - note: infix operator -= is equivalent of x.difference_update(y).  This is outlined below:
 
    >>> x = set([1,2,3,4,5,6])
    >>> y = set([100,200,300,5,6])
    >>> x.difference_update(y)
    >>> x
    {1, 2, 3, 4}
    >>> z = set([1,2,3,4,5,6])
    >>> z -= y
    >>> z
    {1, 2, 3, 4}
    >>> z == x
    True
    
    # Here you can see the difference explicitly in x - y vs x-= y
    >>> x = {100, 200, 300}
    >>> y = {300, 400, 500}
    >>> z = x.copy()
    >>>
    >>>
    >>> x
    {200, 100, 300}
    >>> y
    {400, 300, 500}
    >>> z
    {200, 100, 300}
    >>> x - y
    {200, 100}
    >>> new = x - y
    >>> id(new)
    1517543477984
    >>> x -= y
    >>> id(x)
    1517543478656
"""

------------------------------------------------------------------------------

"""
frozen set vs set functions & public interface:

# using sets to remove duplicates! :)

difference = set(dir(set()).difference(set(dir(frozenset())))

    >>> print(difference)
    {'__iand__',
     '__ior__',
     '__isub__',
     '__ixor__',
     'add',
     'clear',
     'difference_update',
     'discard',
     'intersection_update',
     'pop',
     'remove',
     'symmetric_difference_update',
     'update'}
     
     # As we can see above, frozen sets being immutable they cannot modify the set after creation!
     # It is still possible for things like x.difference(y) where x is type: frozenset
     # However, note the __isub__ dunder difference, x -= y (surprisingly?) does actually work... but it returns
     # a new frozenset under such circumstances.
     # This is because when dunder __isub__ is not implemented on an object, the dunder __sub__ is a fallback
     
     >>> class Augment:
    ...     def __sub__(self, other):
    ...             print('dunder sub')
    ...     def __isub__(self, other):
    ...             print('dunder isub')
    ...
    ...
    >>> var = Augment()
    >>> var - None
    'dunder sub'
    >>> var -= None
    'dunder isub'
    
    >>> class NoAugment:
    ...     def __sub__(self, other):
    ...             print('normal dunder sub...')
    ...
    ...
    >>> var = NoAugment()
    >>> var -= None
    'normal dunder sub...'
    
     # Here we can see, frozenset class does NOT have an implementation of dunder isub:
     >>> print(dir(frozenset()))
    ['__and__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__or__',
     '__rand__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__ror__',
     '__rsub__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__xor__',
     'copy',
     'difference',
     'intersection',
     'isdisjoint',
     'issubset',
     'issuperset',
     'symmetric_difference',
     'union']
     
     # and set() does:
     >>> print(dir(set()))
    ['__and__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__iand__',
     '__init__',
     '__init_subclass__',
     '__ior__',
     '__isub__',
     '__iter__',
     '__ixor__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__or__',
     '__rand__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__ror__',
     '__rsub__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__xor__',
     'add',
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
     
     So when we ask a frozen set to perform -= it actually falls back to performing x - y and returns a new frozenset.
     
"""

------------------------------------------------------------------------------


"""
set discard(elem) function:
 - Discards an element from the set
 - Unlike remove(elem), does NOT raise a KeyError if the elem is not present in the set
    >>> x = {1,2,3}
    >>> x.discard(4)
    >>> x.remove(4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 4
 -- Big O Notation: Discarding (like removing) an element from the set is constant time O(1).
"""

"""
Guarantee of set order cannot be assured.  Sets by default are length 8 in size, after filling to a certain percentage
the order in which.  Here we can see the set resizing when the 5th element is added:

    >>> x = set()
    >>> get_size(x)
    216
    >>> x.add(1)
    >>> x.add(2)
    >>> x.add(3)
    >>> x.add(4)
    >>> get_size(x)
    216
    >>> pprint(x)
    {1, 2, 3, 4}
    # Still 216 bytes until we add one more:
    
    >>> x.add(5)
    >>> get_size(x)
    728  # Finally resized! Note this resizing looks to approximately 3.37~ %
    
    We can see that the order of the iterable is not guaranteed within sets in python:
    some_list = [1,2,20,210,6,100]
    >>> some_list = [1,2,20,210,6,100]
    >>> set(some_list)
    {1, 2, 100, 6, 210, 20} # not the same as the sequenced list

"""


------------------------------------------------------------------------------

"""
TLDR Notes:
# Two types of built in set (set() / frozenset())
# Create sets using set(iterable), frozenset(iterable), {n,...}
# By default, empty braces will create a dictionary (care) = {} # Type Dict, not an empty set!
# By default, python sets are allocated sizing for 8 elements. 
# By default, resizing occurs when the set is 60%~ (TODO FIX THIS) full? seems to resize 3.5x its size?
# Sets cannot guarantee the order of elements, resizing etc can shift the order completely
# Comparison of sets, cares not about order of elements - only the elements within explicitly.
# set.difference() returns a set with the elements from x that are not in *others
# set.difference() is equivalent to using '-' (x - y - z) and this is due to a dunder __sub__ implementation
"""