"""
Objects in python are never 'explicitly' destroyed.  However when they become unreachable, they may be garbage
collected.  An implementation is allowed to postpone garbage collection or omit it altogether.

Note: CPython implements are 'reference counting' with optional delayed detection / threshold detection of cyclically
linked garbage.  Other python implementations vary and the CPython implementation is subject to change.

Garbage collection does tend to collect (most) objects as soon as they become unreachable - the reference counting
mechanism outlined above, however there is no guarantee that objects containing circular references will be collected.
Think of a list whos first element was a reference to the list itself as an example.  You should not depend that
CPython will garbage collect and force finalization of objects explicitly, things such as files should always be
explicitly closed by the user.  sys.getrefcount() can be used as a subtle indicator to view total number of references
however be aware the check in itself holds a reference, so don't be surprised to see (2) when you expect (1).
the weakref module can be used to create weak references to objects.  Both of these are demonstrated below:
"""

import sys
import gc


class Custom:
    ...


c1 = Custom()
print(len(gc.get_referrers(c1)))
print(sys.getrefcount(c1))

# 1
# 2 (sys.getrefcount(obj) holds a reference temporarily in itself, this is why you should -1 from the result.
