"""
Sets in python have a complex inheritance tree of abstract base classes.  As we know, sets themselves are mutable, evidenced
by the `add`, `remove` and `discard` methods respectfully.  This document outlines the complex inheritance tree and where
certain capabilities of the `Set` class are derived.
"""

from collections.abc import Set

Set.__mro__

# <class 'collections.abc.Set'>
# <class 'collections.abc.Collection'>
# <class 'collections.abc.Sized'>
# <class 'collections.abc.Iterable'>
# <class 'collections.abc.Container'>
# <class 'object'>


# Set(Collection) -> Collection(Sized, Iterable, Container)


# Set `is-a` Collection
# `Collection` is a collection of (`Container`, `Iterable` & `Sized`) respectively.


# Set `is-a` Container
# It inherits the `__contains__` functionality to use in conjunction with `in` and `not in`
x = {1,2,3,4,5}
5 in x # True
10 not in x # False

# Set `is-a` Iterable
# It inherits the __iter__ functionality to use with `for in`
for n in set(range(100):
    print(n)  # prints (, 2, 3, 4, ..., 97, 98, 99)
    
# Set `is-a` Sized
# It inherits the __sized__ functionality to use with len(set_instance)
len(set{"a", "b", "c", "c", "b", "c"})  # 3
