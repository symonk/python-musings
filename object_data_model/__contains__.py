"""
Dunder __contains__() is called by the `in` keyword (and respectively when `not in` is called).
The check is called on the object on the right hand side of the expression.

dunder __contains__() is exposed via the `collections.abc.Container` abstract base class
which using a dunder __subclasshook__ which at runtime considers any object implementing __contains__
as a subclass of itself.

dunder __contains__(x: Any) by its contract should return a boolean value if 'x' is considered
in the container, however; in the event a non bool is returned; bool(return_val) is called

In the event that no __contains__() is implemented in the object; python will firstly attempt
the new iterator protocol via __iter__() and then backing off to the old style __getitem__.
This means that by default, in checks will raise a TypeError on user defined objects as they 
are by default; not iterable.
"""


# Python default implementation of contains returns False for all objects

def __contains__(self, x):
  return False
  
  
class X:
  def __contains__(self, x):
    return [1,2,3] # all checks would return True
    return [] # all checks would return False
    
    
class UserDefined: pass

'y' in UserDefined()  # TypeError: Argument of type 'UserDefined' is not iterable



class UserDefinedIter:
    def __iter__(self):
      print('using dunder __iter__')
      return iter('y')
    def __getitem__(self, idx):
      print('using dunder __getitem__')
      return 'y'
      
'y' in UserDefinedIter()  # Using dunder __iter__; # True

class OldGetItemOnly:
  def __getitem__(self, idx):
    return 'y'

'y' in OldGetItemOnly()  # True

