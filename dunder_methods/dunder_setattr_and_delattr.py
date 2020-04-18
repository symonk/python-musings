"""

dunder setattr (__setattr__): Called when attribute assignment is attempted, args: (key, value)
dunder delattr (__delattr__: Called when attribute deletion (del x) is attempted, args: (item)

"""


class SetAttr:
    def __setattr__(self, key, value):
        print(f"Attribute setting attempted: k: {key} ~ v: {value}")


s = SetAttr()
setattr(s, 'name', 10)
s.name = 'hello'

"""
Results in:

Attribute setting attempted: k: name ~ v: 10
Attribute setting attempted: k: name ~ v: hello

"""


class DelAttr:

    def __delattr__(self, item):
        print('Attempted to delete attr: %s' % item)


d = DelAttr()
del d.x


"""
Results in:

Attempted to delete attr x

"""
