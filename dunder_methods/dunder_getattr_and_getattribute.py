"""
dunder getattribute (__getattribute__)
dunder getattr (__getattr__)

getattribute:  Called to implement attribute access to the class, if the class implements __getattr__ it will not be
called unless __getattribute__ explicitly calls it, or raises an AttributeError
"""


class AccessAttr:
    def __init__(self):
        self.att = 'att'

    def __getattribute__(self, item: str):
        if item == 'att':
            return super().__getattribute__(item) # notice returning self.att would end in infinite recursion
        raise AttributeError(f"No such attribute {item}, only 'att' exists here.")


attr = AccessAttr()
print(attr.att)
attr.nothing

"""
Results in:

att
Traceback (most recent call last):
  File "C:/workspace/learning-python/dunder_methods/dunder_getattr_and_getattribute.py", line 22, in <module>
    attr.nothing
  File "C:/workspace/learning-python/dunder_methods/dunder_getattr_and_getattribute.py", line 17, in __getattribute__
    raise AttributeError(f"No such attribute {item}, only 'att' exists here.")
AttributeError: No such attribute nothing, only 'att' exists here.

"""


class AttrAndAttribute:
    def __init__(self):
        self.x = 1
        self.y = 2

    def __getattribute__(self, item):
        item = super().__getattribute__(item)
        if item:
            return item
        raise AttributeError(f"{item} does not exist here")

    def __getattr__(self, item):
        print('__getattribute__ raised an AttributeError, i will handle it!')
        return self.__dict__.get(item, None)


a = AttrAndAttribute()
print(a.x)
print(a.y)
print(a.z)

"""
Results in:

1
2
__getattribute__ raised an AttributeError, i will handle it!
None

"""
