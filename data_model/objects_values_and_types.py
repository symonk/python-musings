"""
Objects are pythons abstraction for all data.  All data in a python program is represented by objects or relationships
between objects.

In Python, every object has the following:
 - A Type
 - A Value
 - An identity (id)

Upon creation, an objects identity or type can never be changed, however its 'value' can in some instances, this is
outlined in more detail later.
Specifically in CPython you can think of the id of an object as its address in memory, for example:

x = 'hello world'
id(x)  # is the address in memory where x is stored.

The objects type determines the operations in which it supports, for example does it have a length?  The type() function
returns the objects type, for example:

type(25) # <class 'int'>
note: This 'type' above actually is an object in itself.

Objects values can sometimes be changed, when the value of an object can be changed, we refer to such objects as
'mutable'.  When the value(s) of the object cannot be changed, we refer to these as 'immutable'.

Note: A custom container type for example, that when created does not change BUT holds references to other mutable
types, is also said to be deemed immutable.  So immutability is not as strict as you might think, its more subtle
that than.  A short example of this is outlined below:
"""

# dictionaries and lists in python are considered mutable as their value(s) can be modified after creation
mutable_type = dict(a=1, b=2)

# tuples (below) are immutable in python (as are numbers and strings)
immutable_type = (10, 25, mutable_type)

# So if you think of mutability in the strictest of sense, you may assume a tuple containing a list or dictionary
# is actually, 'mutable'?  In python even tho the objects that the immutable container has a reference to can change
# we still deem such objects as 'immutable'.  This is outlined below:
print(immutable_type)
# (10, 25, {'a': 1, 'b': 2})

mutable_type['new'] = 'value'
print(immutable_type)
# (10, 25, {'a': 1, 'b': 2, 'new': 'value'})

"""
As you can see above, the immutable 'tuple' structure, holds a reference to a 'mutable' dictionary.  When we change the
data in the dictionary, the tuple reflects such state.  Since the actual elements contained in the tuple cannot be 
modified after creation e.g added or removed, we still consider it to be an immutable type.
"""



