"""
dunder call (__call__) is used to mark something as callable.  To check the callability of an object in python we
can use the callable(obj) built-in.  This returns True or False, depending on if the object is callable or not.
"""


class BasicCallable:
    def __call__(self, *a, **kw):
        # instance method
        print(f"called with args: {a} and kwargs: {kw}")


b = BasicCallable()
print('-----')
b(100, 200, a=300, b=400)

"""
Results in:

-----
called with args: (100, 200) and kwargs: {'a': 300, 'b': 400}

"""

"""
Often with your own custom classes; __call__ can be overkill as its an instance method and you are much better
just implementing a standard instance-method for the same purpose. as outlined below:

"""


class Obscure:
    def __init__(self, color: str = 'red'):
        self.color = color

    def __call__(self):
        return self.color.upper()

    def get_upper_color(self):
        return self.color.upper()


print('-----')
one = Obscure()
print(one())
two = Obscure()
print(two.get_upper_color())

"""
Results in:

-----
RED
RED

"""

"""
Which one is better? obviously the instance method!
In order to check if something is callable, we can use the built in callable keyword as demonstrated below:
"""

print('-----')
# all classes are callable
print(callable(Obscure))
# because we implemented __call__ our INSTANCE is also callable
print(callable(Obscure()))
# functions are callable


def x():
    pass


print(callable(x))


class newclazz:
    pass


print(callable(newclazz()))
print(callable(lambda anon: anon))

"""
Results in:

-----
True
True
True
False
True

So why are all functions and classes callable by default?

"""


def y():
    pass

print('----')
print(y.__call__)

"""
----
<method-wrapper '__call__' of function object at 0x000002375EE24488>
"""
