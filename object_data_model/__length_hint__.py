"""
dunder __length_hint__() is used in conjunction with the operator.length_hint() function.
This function should return an `estimated` length of the object; but can also return `NotImplemented`
in order to appear as if __length_hint__() is not implemented at all.

Similarly to dunder __len__() the length must be >= 0.  The method is considered for optimization
purposes only and never for correctness.

If both dunder __len__() and __length_hint__() are implemented, operator.length_hint() will defer to
dunder __len__().

operator.length_hint() returns 0 if neither dunder __len__ nor dunder __length_hint() are defined.
"""


from operator import length_hint


class SimpleLengthHint:
  def __length_hint__(self) -> int:
    return 100
  def __len__(self) -> int:
    return 105
    
length_hint(One()) # 105
len(One())  # 105

class LengthHint:
  def __length_hint__(self) -> int:
    return 1337
    
length_hint(LengthHint()) # 1337
len(LengthHint()) # TypeError: Object of type 'LengthHint' has no len()
