import random
import string
from typing import Tuple


"""
Dunder __dir__ is called on objects using the dir(obj) syntax.  The return value of dunder __dir__ should be a
sequence (ideally a list) as python will do two things here:

1) Convert the sequence to a list
2) Sort the list

If the built in dir() is invoked without any arguments, it will return the items in local scope.

If an object omits an explicit __dir__ then python will attempt to take a best guess using obj.__dict__ and
the type.

"""


def local_scope(x: int = 100):
    a, b, c = 1, 2, 3
    print(dir())


def custom_dir():
    class MyDir:
        def __dir__(self) -> Tuple:
            # we will return a tuple here; to see pythons implicit conversion.
            return tuple([random.choice(string.ascii_lowercase) for x in range(13)])

    print(dir(MyDir()))
    print(type(dir(MyDir())))


if __name__ == '__main__':
    local_scope(x=1337)  # ['a', 'b', 'c', 'x']
    custom_dir()
    # ['d', 'e', 'f', 'g', 'h', 'k', 'l', 'l', 'n', 's', 's', 't', 'y']
    # <class 'list'>
