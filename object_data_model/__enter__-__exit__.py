"""
The context manager protocol in python is how custom objects can interact with the `with obj as x` syntax.
Using such statement the return value of dunder __enter_ is bound to the `as x` variable.  Upon completion of
the with block, dunder __exit__ is automatically invoked.  In the event an exception is raised is the runtime context
then exc_type, exc_value & traceback will hold the exc information (otherwise all are None) if no exception was raised.

Note: Context managers should NOT be responsible for reraising an exception in a dunder __exit__, that is the callers
responsibility; However should they choose to suppress it; returning a True `truthy` value will suppress such exception
and carry on execution, False return values in __exit__ will raise such exception after the fact.

Note: If the suite is exited via any other means than an exception; the return value of __exit__ is ignored.
"""


from __future__ import annotations

from typing import Optional
from typing import Type


class ContextManager:
    def __enter__(self) -> ContextManager:
        return self

    def __exit__(self, exc_type: Optional[Type[ValueError]], exc_value: Optional[BaseException], traceback) -> bool:
        print(f"Exiting: {exc_type} {exc_value} {traceback}")
        return False


class ExcSuppressingCtx:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        print(f"Exiting.. (silently)", locals())
        return True


if __name__ == '__main__':
    with ContextManager():
        # no exception
        ...
    # Exiting: None None None

    with ExcSuppressingCtx() as ctx:
        raise ValueError("silently suppressed!")
    #

    with ContextManager() as ctx:
        raise ValueError("one two three")
    # Exiting.. (silently) ...
