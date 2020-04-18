"""
We often refer to __init__ as the 'constructor' method because we are so familiar with other languages, however
__init__ is responsible for initializing an already instantiated instance.  The first port of call for actually
instantiating the object instance begins at __new__.  This is actually a class method (requiring cls) and should
return an instance of the class, when returning such instance __init__ is automatically called, if __new__
fails to return a new instance, __init__ will not be called.  Notice how the typical signature of __init__ is to
pass in (self), whereas __new__ requires cls.  Another interesting note on __new__ is that it can be used to
return an instance of ANOTHER object, in this instance isinstance() checks fail and __init__ is never called.
"""


class NeverCalled:
    def __new__(cls):
        return 'word'  # return a word!

    def __init__(self):
        print('never called!')


a = NeverCalled()
print(type(a))

"""
output (notice: 'never called!' is non existent:

<class 'str'>
"""

"""
Lets fix this to do as you probably already know
"""


class Called:
    def __new__(cls):
        return super().__new__(cls)

    def __init__(self):
        print('called now!')


print('----------------')
c = Called()
print(type(c))

"""
----------------
called now!
<class '__main__.Called'>
"""

"""
Now to get some arguments into our instances, we can use the simple idiom of *args and **kwargs
"""


class ArgAndKwarg:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return super().__new__(cls)


c = ArgAndKwarg()
print('---')
c2 = ArgAndKwarg(15, 20, 25)
print('---')
c3 = ArgAndKwarg(10, hello='hey', goodbye='bye')

"""
results in:

<class '__main__.Called'>
()
{}
---
(15, 20, 25)
{}
---
(10,)
{'hello': 'hey', 'goodbye': 'bye'}

Process finished with exit code 0

"""
