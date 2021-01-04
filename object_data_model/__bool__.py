"""
Dunder __bool__ is used to implement custom `truthy` testing.  bool(obj) is the built in function 
that will call an objects dunder __bool__ implementation.

In the event that dunder __bool__() is not defined; dunder __len__() will be invoked by the bool(obj)
built in.  In this scenario; the object is considered `True` if dunder __len__() returns a non-zero
value.

If a class does not define dunder __bool__() OR dunder __len__() then all of its instances are considered
`True`.


class Both:
  """
  As you can see here; bool is implemented so __len__() is not accounted for when bool(Both()) is called.
  """
  def __len__(self) -> int:
    return 0
    
  def __bool__(self) -> bool:
    return True
    
    
class LenOnly:
  def __len__(self) -> int:
    # return -1 raises a ValueError in python; positive integers only
    # return 0; would create bool(LenOnly()) to be False
    return 1 # All instances of LenOnly are `True`

class BoolOnly:
  def __bool__(self) -> bool:
    # return False; all instances would be considered False
    return True; all instances of BoolOnly are `True`
    
class Default:
  # By default; no dunder __len__() or __bool__() will result in instances being `True`
  ...
  
