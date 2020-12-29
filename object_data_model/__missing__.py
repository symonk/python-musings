from collections import defaultdict
"""
Invoked by subclasses of dict when dunder __getitem__ when they key is not present in the dictionary.
This method is only applicable to dictionary subclasses (as outlined below) as base dict class invokes it and
subsequently raises a KeyError if the default_factory in subclasses of the collections.defaultdict.
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
