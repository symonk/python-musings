"""
Dunder repr (__repr__) is supposed to be unambiguous, this means it should give a programmer-level description of the
class, typically something similar to what it would involve in order to recreate it.  __repr__ is called by the built
in method: repr(obj) and you should make it a force of habit for all custom classes to implement a __repr__.  When
a __str__ method is non existing, print() functions will defer to __repr__.  __repr__ is required to return a string.
__repr__ is typically used a debugging tool, so the string returned here should be very informative.
"""


class MyRepr:
    def __init__(self):
        self.number = 10
        self.word = 'word'

    def __str__(self):
        return 'This is used for numbers and words'

    def __repr__(self):
        return f"type: {type(self).__name__} - (number: {self.number}, word: {self.word})"


class DefaultRepr:
    pass
    #  Default repr psuedo code:
    #    {0}.{1} object at {2}
    #    {0} = self.__module__
    #    {1} = type(self).__name__
    #    {2} = hex(id(self))


class WithoutStrPrinting:
    def __repr__(self):
        return 'no str was defined; here is repr instead!'


myrepr = MyRepr()
print(repr(myrepr))
print(myrepr)

print('----')
print(repr(DefaultRepr()))
print('^ above is: module name, type of the instance name, and hex converted id of the object')

print('-----')
print(WithoutStrPrinting())

"""
Results in:

type: MyRepr - (number: 10, word: word)
This is used for numbers and words
----
<__main__.DefaultRepr object at 0x00000236F2E61898>
^ above is: module name, type of the instance name, and hex converted id of the object
-----
no str was defined; here is repr instead!

"""
