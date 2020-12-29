"""
Part of the object access protocol.  Called unconditionally for attribute access on instances of the class.
If the instance also defines a __getattr__, it will not be invoked unless __getattribute__ explicitly raises
an `AttributeError` or calls explicitly calls __getattr__() itself.  When successful it should return the 
computed attribute value for `name`.

In order to avoid infinite recursion in __getattribute__ it should call the base class. 

All of this is outlined below
"""

# __getattribute__ calling __getattr__ implicitly by the super() call to __getattribute__ raising the AttributeError.

"""
In [81]: class A:
    ...:     def __init__(self):
    ...:         self.a = 100
    ...:         self.b = 200
    ...:     def __getattribute__(self, name):
    ...:         print(f"dunder getattribute for: {name}")
    ...:         attr = super().__getattribute__(name)
    ...:         return attr
    ...:     def __getattr__(self, name):
    ...:         print("The dunder __getattribute__ super call implicitly raises
    ...:  an AttributeError so this gets called and 1337 returned.")
    ...:         return 1337
    
    
In [82]: obj = A()

In [83]: obj.a
dunder getattribute for: a
Out[83]: 100

In [84]: obj.b
dunder getattribute for: b
Out[84]: 200

In [85]: obj.c
dunder getattribute for: c
The dunder __getattribute__ super call implicitly raises an AttributeError so this gets called and 1337 returned.
Out[85]: 1337

"""

# __getattribute__ called for attribute access unconditionally.

"""
In [104]: class GetAttribute:
     ...:     def __init__(self, x, y) -> None:
     ...:         self.x = x
     ...:         self.y = y
     ...:     def __getattribute__(self, name):
     ...:         print(f"In __getattribute__, looking up {name}")
     ...:         return super().__getattribute__(name)


In [100]: ga = GetAttribute(5, 15)

In [101]: ga.x
In __getattribute__, looking up x
Out[101]: 5

In [102]: getattr(ga, 'x')
In __getattribute__, looking up x
Out[102]: 5

In [103]: ga.__dict__['x']
In __getattribute__, looking up __dict__
Out[103]: 5
"""

