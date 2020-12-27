"""
Similar to metaclassing, __init_subclass__ can be used to customise class creation.  Whenever class B inherits from
class A, __init_subclass__ is called on that class, this makes it possible to change the behaviour of subclasses.
Similar to class decorators (tho they only impact the class they are decorating, this affects all future subclasses).

__init_subclass__ should ideally be implemented as using the @classmethod (descriptor impl), however if excluded
then the function is implicitly converted to a class method.

by default the object.__init_subclass__ does nothing, except raise an exception if it is called with any arguments.

"""


class NotPreferred:

    def __init_subclass__(cls, **kwargs):
        # Not preferred, should use the @classmethod to avoid confusion around implicit conversion.
        print(cls.__init_subclass__)  # Bound method NotPreferred.__init_subclass__


class Preferred:

    @classmethod
    def __init_subclass__(cls, **kwargs):
        # preferred, no under the hood implicit conversion.
        cls.name = kwargs.pop("name")


class SubClass(NotPreferred):
    ...


class SubClassTwo(Preferred, name="Cool!"):
    ...


class ArgsToObjectDunderRaises(name='test'):
    ...


if __name__ == '__main__':
    one = SubClass()
    two = SubClassTwo()
    print(two.name)
    ArgsToObjectDunderRaises()  #TypeError: __init_subclass__() takes no keyword arguments.
