"""
dunder init (__init__) is the bread and butter of any custom class you will create, before understanding __init__
it is important to understand __new__ (go read my docs on that one).  If you look closely at the signature, __init__
takes ina 'self' parameter, this is an instance method - and that tells us an awful lot.  The instance already exists
by the time we enter __init__.  so it is NOT used to actually create an instance, but to initialize an instance once
it has already been created.

Below we can demonstrating initializing an instance of our new Dog class:

"""


class Dog:
    def __init__(self, breed: str, weight_in_lbs: float):
        # here we already have an instance of dog created
        print(type(self))
        self.breed = breed
        self.weight_in_kg = weight_in_lbs / 2.2  # trivial but just an example


alsation = Dog('Alsation', 220)
print(alsation.breed)
print(alsation.weight_in_kg)

try:
    Dog.breed
except AttributeError:
    print('Dog doesnt have a breed, its a class.  remember we need an instance of dog!')


print('-----')
"""
Here we can see, the type of self is already a 'Dog'

<class '__main__.Dog'>
Alsation
99.99999999999999
Dog doesnt have a breed, its a class.  remember we need an instance of dog!

Here is a quick outline if we wanted to use class variables, these are similar to 'static' variables in other languages
"""


class BigGun:

    def __str__(self):
        return 'I am a big massive gun!'


class SmallGun:

    def __str__(self):
        return 'I am only a small gun'


class ArmyTank:
    big_gun = BigGun()

    def __init__(self):
        pass


print('----')
a = ArmyTank()
print(a.big_gun)
print(ArmyTank.big_gun)

print('----')
# but be careful!
ArmyTank.big_gun = SmallGun
print(ArmyTank().big_gun)
print('Yikes! ^ all instances have been secretly change(d) and persist the value')

"""
Results in :

----
I am a big massive gun!
I am a big massive gun!
----
<class '__main__.SmallGun'>
Yikes! ^ all instances have been secretly change(d) and persist the value

"""

"""
no non-None is permitted to be returned from __init__(), doing so will raise a TypeError as shown below:
"""


class ReturnInInit:
    def __init__(self):
        return True


print('----')
a = ReturnInInit()

"""
Traceback (most recent call last):
  File "C:/workspace/learning-python/dunder_methods/dunder_init.py", line 97, in <module>
    a = ReturnInInit()
TypeError: __init__() should return None, not 'bool'
"""

"""
When dealing with inheritance in python, it is explicitly required that super() inits are invoked in the derived classes.
This is demonstrated below:

"""


class Base:
    def __init__(self, *a, **kw):
        print('This is base')


class A(Base):
    def __init__(self, *a, **kw):
        print('I wont invoke super')


class B(Base):
    def __init__(self, *a, **kw):
        print('I will invoke super')
        super().__init__(*a, **kw)


new_a = A()
new_b = B()

"""
Results in:

I wont invoke super
I will invoke super
This is base

"""
