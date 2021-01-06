"""
dunder __str__ is invoked by all three of the following builtin functions:

print(x) | str(x) | format(x).

dunder __str__ should return an 'informal' nicely printable string representation of the object.
dunder __str__ should return a string.

"""

class CustomObject:
  def __init__(self, x: int, y: str) -> None:
    self.x = x
    self.y = y
    
 def __str__(self) -> str:
  return f"Custom object with x: {self.x} | y: {self.y}"
  
"""  
In [6]: str(CustomObject(1,1))
Out[6]: 'Custom object with x: 1 | y: 1'

In [7]: print(CustomObject(1,2))
Custom object with x: 1 | y: 2

In [8]: "My String: {}".format(CustomObject(100, 200))
Out[8]: 'My String: Custom object with x: 100 | y: 200'


"""
