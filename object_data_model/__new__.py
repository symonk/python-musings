from __future__ import annotations
from typing import List
from typing import Tuple
from typing import Any
from typing import Mapping
from typing import Optional


"""
object.__new__(cls, [...])

Called to instantiate a new instance of `cls`.  __new__ should return (not but always) an instance
of the `cls`.  If the return value of __new__ is an instance of cls (or a subclass of it) then the instances
__init__ method is automatically called by python with the same arguments passed into __new__, however since
__init__ is invoked post-instance creation, `self` is passed to __init__ and self is the instance that __new__'s
super call just created.

Some common uses of custom __new__ implementations are:
 -> Metaclasses.
 -> Creating subclasses of immutable types (e.g int) and hooking into instance creation.
"""


class SimpleObject:
    """
    Like 99% of your python classes, custom __new__ implementations are relatively bespoke and often unnecessary.
    This class works just fine and has no pre/post instance manipulation from a __new__ implementation.  Instead it
    uses objects __new__ by default, implicitly.
    """
    def __init__(self, x: int, y: str, z: Optional[List[int]] = None) -> None:
        self.x = x
        self.y = y
        self.z = z or []


class NewReturningInstanceOfCls:
    """
    Occasionally there is some necessity or need to do some logic pre-object instantiation (or post but pre-init).
    This class allows you to hook in prior to dunder init and do some processing at instance creation time.
    """

    def __new__(cls, a: int, b: str) -> NewReturningInstanceOfCls:
        instance = super().__new__(cls)
        return instance

    def __init__(self, a: int, b: str) -> None:
        self.a = a
        self.b = b
        print("Dunder init was invoked, this is because dunder __new__ returned an instance of this class.")
        print(vars(self))


class NewReturningSubClass:
    """
    Dunder __new__'s contract states it (should) return an instance of cls, or a subclass of cls if the
    auto invocation of dunder __init__ is wanted.
    This class returns a subclass of NewReturningSubclass, to prove that __init__ is still called.
    """
    def __new__(cls, *args, **kwargs) -> SubClazz:
        # cls is redundant, we will patch in a subclass.
        return super().__new__(SubClazz)

    def __init__(self, *args) -> None:
        self.x = args[0]
        print("Dunder init was invoked, this is because dunder __new__ returned a subclass of this class.")
        print(vars(self))


class SubClazz(NewReturningSubClass):
    ...


class NewWithoutInit:
    """
    In this class instance, dunder __new__ fails to return either an instance of cls or a subclass.
    We can see that object initialization is skipped here, __init__ is never called and nothing is printed to stdout.
    """
    def __new__(cls, *args: Tuple[Any], **kwargs: Mapping[Any, Any]) -> Tuple[str, int]:
        return 'foobar', 42

    def __init__(self, *args) -> None:
        print("No printing will happen here, type(self) != NewWithoutInit", *args)
        raise Exception("This is not raised!")


if __name__ == "__main__":
    simple = SimpleObject(x=1, y='foo', z=[1, 2, 3])
    instance = NewReturningInstanceOfCls(a=100, b='hello')
    sub_clazz = NewReturningSubClass(1337)
    no_init = NewWithoutInit()