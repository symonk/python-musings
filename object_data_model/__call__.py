"""
Dunder __call__() is called when the object is called, similar to a function do_something(x,y,z).
By default classes are callable; however by implementing dunder __call__() instances can become callable.

collections.abc.Callable can be used to check if something is callable; like a lot of the collections
modules in python it relies on use of __subclasshook__ dunder method to smartly check if something is
considered callable or not.

calling () on a instance which does not implement dunder __call__() will raise a TypeError `object is not callable`
"""


from collections.abc import Callable

"""
By default, classes are `Callable`, however to provide our own functionality to an instance of our classes
we can implement dunder `__call__` as outlined below:
"""


class MyClass:
    pass


print(callable(MyClass))  # True
print(callable(MyClass()))  # False


class MyNewClass:
    def __call__(self, *args, **kwargs):
        return "foobar" in kwargs


print(callable(MyNewClass))  # True
print(callable(MyNewClass()))  # True
print(MyNewClass()(foo=1, bar=2, foobar=3))  # True!
