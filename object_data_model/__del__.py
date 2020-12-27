from sys import getrefcount

"""
Another core part of object customisation is the dunder __del__ (finalizer).  This is called when an object is about
to be destroyed.  If a base class implements a custom __del__ implementation, derived subclasses of the base should
ensure to call super().__del__() to ensure proper deletion of the base class parts of the instance.

It is possible for the dunder __del__ to postpone destruction of the instance by creating a reference to it.  This is
made possible because a common confusion around __del__ is that it is called by syntax like:

x = Klazz()
del x

Postponing this destruction is known as object resurrection and is as an implementation detail on whether python will
attempt to call __del__ twice under such circumstances, CPython will only invoke __del__ once.  Generally doing this in
practice is typically frowned upon.

This is not quite true (as outlined below).  Calling del obj reduces the reference count by 1.  When the reference
count for the instance reaches 0, the dunder __del__ is finally invoked by python.
"""


class BasicDel:
    def __init__(self) -> None:
        self.x = 100

    def __del__(self) -> None:
        print(f"Running: {self.__class__} finalizer")


def demonstrate_reference_count() -> None:
    """
    This function demonstrates that all del x calls, do NOT invoke the dunder __del__ method, but instead decrement
    the object reference count by 1, until the reference count reaches 0 under which circumstances the __del__
    is called.
    :return: None
    """
    one = BasicDel()
    print(getrefcount(one) - 1)
    two = one
    print(getrefcount(two) - 1)
    three = two
    print(getrefcount(three) - 1)
    del three  # ref count = 2, no __del__ called
    del two  # ref count = 1, no __del__ called
    del one  # ref count = 0, __del__ called.


if __name__ == '__main__':
    demonstrate_reference_count()
