from collections import defaultdict
"""
__missing__ is only applicable for subclasses of dictionaries, noticiby the defaultdict (collections.defaultdict) which
accepts a default_factory= callable to its constructor (__new__ -> __init__).  When a default_factory callable is not
supplied, upon key misses as part of __getitem__ then subsequently __missing__ a KeyError is raised.  However, passing a
callable (such as a lambda) to `default_factory=lambda: 1337` then such function is called rather than raising a KeyError
in the instance outlined above.  __missing__ is only applicable to dictionaries specifically and trying such mechanism
on a list subclass (which also supports key indexing) will not work, as __missing__ will never be invoked.  This is all
outlined below.
"""


class CustomDict(dict):
    def __missing__(self, key):
        return 1337


class OnlyDict(list):
    def __missing__(self, key):
        return 999


class DefaultD(defaultdict):
    def __init__(self, default_factory=None, **kwargs):
        super().__init__(default_factory, **kwargs)


if __name__ == '__main__':
    dd = CustomDict(a=1, b=2)
    print(dd['x'])  # 1337
    ll = OnlyDict([1, 2, 3, 4, 5, 6])
    y = ll[10]  # IndexError: list index out of range
    defaultd = DefaultD(default_factory=lambda: 1000)
    print(defaultd['madeup'])  # 1000
    print(DefaultD()['no'])  # No factory callable; raises KeyError
