"""
dunder dir (__dir__) is invoked by the built in dir(object) | dir() keyword (no args necessary).  As per the contract
of dir() a sequence must be returned from any implementations.  dir() automatically converts the sequence to a list
and sorts it; thus it is probably wise to just return a list yourself.

By default dir() will return all the names in the local namespace.
this allows objects to customize the __getattr__ and __getattribute__ to control the way dir() reports their attributes
"""
the_global = 'global'


def dir_namespace():
    x = 1
    y = 'inside'
    print(dir())


# notice, no the_global here.
# ['x', 'y']
dir_namespace()


class A:
    pass

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
print(dir(A))


class Custom:
    def __init__(self):
        self.x = 100
        self.y = 'y'

    def do_something(self):
        pass

    def __dir__(self):
        return {'zebra', 'alpha'}


print('----')
print(dir(Custom()))

"""
Results in:

----
['alpha', 'zebra'] # notice the alphabetically converted list(it was a set originally)
"""
