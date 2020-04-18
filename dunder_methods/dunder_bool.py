"""
Dunder bool (__bool__) is useful for discovering the falsy/truthy state of the given object.  This is called using
the built in bool(obj) method and has a few conditions used to determine such value(s).  As per its contract, __bool__
should return either True or False.  If __bool__ is not implemented, python will defer to the objects __len__ method
and if that returns a non-zero will return True, else False.  Important:  If a class (by default all your custom classes)
do NOT implement either __len__ or __bool__ they will automatically be considered True.
"""


class Both:
    def __len__(self):
        return 0 # False

    def __bool__(self):
        return True # we want it to be true regardless :)


print(bool(Both()))


class OnlyLen:
    def __len__(self):
        return 10


print(bool(OnlyLen()))


class OnlyBool:
    def __bool__(self):
        return False


print(bool(OnlyBool()))


class NoneOfThem:
    pass


print(bool(NoneOfThem()))


"""
Results in the following:

True
True
False
True

"""
