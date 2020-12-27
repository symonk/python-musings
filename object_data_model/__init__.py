"""
Called post dunder __new__ when the instance (or subclass) has been instantiated, but before it is returned to the
caller.  Similar to teardown of __del__, if a base class has a __init__ a super().__init__(*args, **kwargs) call
should be explicitly performed to prepare aspects of the base class correctly.

Because dunder __init__ and dunder __new__ work tightly together to create instances of classes, init should
implicitly (or explicitly return) None, otherwise a TypeError is raised at runtime.
"""


class A:
    def __init__(self, x: int) -> None:
        self.x = x
        print('in A')


class B(A):
    def __init__(self, x: int) -> None:
        super().__init__(x)
        print('in B')


class C:
    def __init__(self, x: 100) -> int:
        self.x = x
        return self.x


class ExplicitNone:
    def __init__(self) -> None:
        return None


def inheritance_example():
    B(x=100)


def type_error():
    C(x=1337)  # TypeError: __init__ should return None, not 'int'
    ExplicitNone()


if __name__ == "__main__":
    inheritance_example()
    type_error()
