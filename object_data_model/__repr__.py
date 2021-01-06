"""
dunder __repr__ is called by the builtin repr() function and should 
look like a valid python expression, usable to reconstruct the object.

if a class defines a dunder __repr__() but not a dunder __str__() then
the repr will be called in place of __str__() for things like print(x);
format(x); str(x).

__repr__() is used for debugging and should be unambiguous.
"""

class Train:
  def __init__(self, wheels: int, color: str, power_mechanism: str) -> None:
    self.wheels = wheels
    self.color = color
    self.power_mechanism = power_mechanism
    
 def __str__(self) -> str:
     return f"A {self.power_mechanism} train with: {self.wheels} wheels"
     
 def __repr__(self) -> str:
    return f"Train(wheels={self.wheels}, color={self.color}, power_mechanism={self.power_mechanism})"
    
    
  train = Train(36, 'red', 'steam')
  str(train)  # 'A steam train with: 36 wheels'
  repr(train)  # 'Train(wheels=36, color=red, power_mechanism=steam)
