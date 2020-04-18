"""
In terms of object creation / initialization / deletion, __del__ is the final piece of the puzzle.  __new__ we know
is used to instantiate the instance, __init__ is used to initialize the created instance.  __del__ is considered a
finalizer and gets invoked automatically just prior to garbage collection.  This occurs ONLY when an instantiated object
no longer has any references (getrefcount() == 0 for obj).  Lets demonstrate, but note its also possible to invoke gc
manually, we will demonstrate that too
"""


import sys


class RefToMe:
    pass

    def __del__(self):
        # this only runs when gc runs, not immediately when refcount == 0
        print('destroyed! # class: RefToMe!')


print('-----')
ref = RefToMe()
print(sys.getrefcount(ref))
# wait a minute, the ref count is 2?!
# This is because calling getrefcount() passes the object by reference into the functions args, thus creating 2 refs
# Typically assume true ref count is getrefcount(obj) - 1

"""
Some important notes around __del__
calling del ref here does NOT call ref.__del__ it merely decreases ref count of Ref by -1

see below:
"""


print('-----')


class DelMe:
    def __del__(self):
        print('destroyed! # class: DelMe!')


a = DelMe()
b = a
print('ref count: ' + str(sys.getrefcount(a)))
print('deleting one ref')
del a
print('ref count: ' + str(sys.getrefcount(b)))

"""
Results in:

-----
ref count: 3
deleting one ref
ref count: 2
destroyed! # class: RefToMe!
destroyed! # class: DelMe!
"""
