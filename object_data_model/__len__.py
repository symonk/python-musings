"""
Dunder __len__() is used to implement the builtin len(obj) function.
It should return an integer >= 0, returning a negative integer or 
any other type that cannot be interpreted as an integer; will raise a TypeError.

Called as a backup by the builtin bool(obj) function if the object
in question does NOT implement dunder __bool__() itself.
"""

class Ruler:
  def __init__(self, total: int) -> None:
    self.total = total
    
  def __len__(self) -> int:
    return self.total * 2
    
    
len(Ruler(10)) # 20


class Ruler:
  def __len__(self) -> int:
    return 200.55. 
    
    
len(Ruler())  # TypeError: 'float' cannot be interpreted as an integer
