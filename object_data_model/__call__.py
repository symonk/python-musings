"""
Dunder __call__() is called when the object is called, similar to a function do_something(x,y,z).
By default classes are callable; however by implementing dunder __call__() instances can become callable.

collections.abc.Callable can be used to check if something is callable; like a lot of the collections
modules in python it relies on virtual subclass registration to determine this, as even classes
which do not directly subclass Callable are known as callable.

calling () on a instance which does not implement dunder __call__() will raise a TypeError `object is not callable`
"""


from collections.abc import Callable


class CallableInstance:
  def __call__(self) -> None:
    print("My instance got called")
    
    
    
calling_clazz = CallableInstance()
calling_instanze = calling_clazz()  # My instance got called

issubclass(CallableInstance, Callable)  # virtual subclasses by Callable __subclass_hook__() has occurred and thats how this is viable.


class Callable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __call__(self, *args, **kwds):
        return False

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Callable:
            return _check_methods(C, "__call__")
        return NotImplemented

    __class_getitem__ = classmethod(_CallableGenericAlias)

    
class NoCall:
  ...
  
NoCall()() # TypeError: NoCall object is not callable
