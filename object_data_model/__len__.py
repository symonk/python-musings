"""
Dunder __len__() is used to implement the builtin len(obj) function.
It should return an integer >= 0, returning a negative integer or 
any other type that cannot be interpreted as an integer; will raise a TypeError.

Called as a backup by the builtin bool(obj) function if the object
in question does NOT implement dunder __bool__() itself.

without a dunder __len__() implemenation; a TypeError is raised.

dunder __len__() should stick within the bounds of sys.maxsize in order to avoid
raising OverflowErrors

To avoid such overflowErrors on truth testing.  If int exceeds sys.maxsize; 
implement a dunder __bool__().
"""

class Ruler:
  def __init__(self, total: int) -> None:
    self.total = total
    
  def __len__(self) -> int:
    return self.total * 2
    
    
len(Ruler(10)) # 20


class BrokenRuler:
  def __len__(self) -> int:
    return 200.55. 
    
    
len(BrokenRuler())  # TypeError: 'float' cannot be interpreted as an integer


class NoLen:
  ...
  
len(NoLen())  # TypeError: object of type 'NoLen' has no len()


import sys
class Overflowing:
  def __len__(self) -> int:
    return sys.maxsize + 1

len(Overflowing()) # OverflowError: cannot fit 'int' into an index-sized integer
bool(Overflowing()) # OverflowError: cannot fit 'int' into an index-sized integer


class OversizedWorksWithBool:
  def __len__(self) -> int:
    return sys.maxsize + 1
  
  def __bool__(self) -> bool:
    return True
  
bool(OversizedWorksWithBool()) # True
len(OversizedWorksWithBool()) # TypeError: cannot fit 'int' into an index-sized integer
