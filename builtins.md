# Python Built Ins

Overview of the python built in functions as of python 3.8

## Format is as follows:
- Built in description
- Built in summary
- Code Examples
- Other information


---

### abs()
 - Returns the absolute value of a number, the value may be an integer or a floating point number
 - Returns the distance in number from 0, e.g abs(100) and abs(-100) both return 100.  If the value passed is a complex number, its magnitude is returned.
 abs() can also take any custom object which has an implementation for __abs__()
 
```python
# simple abs
In [1]: abs(100)
Out[1]: 100

In [2]: abs(-100)
Out[2]: 100

# complex abs
In [3]: my_complex = 2+3j

In [4]: type(my_complex)
Out[4]: complex

In [5]: abs(my_complex)
Out[5]: 3.605551275463989

# floating abs
In [6]: abs(-100.252)
Out[6]: 100.252

# custom obj abs and __abs__
In [17]: class Custom:
    ...:     def __abs__(self):
    ...:         return 1000

In [18]: abs(Custom())
Out[18]: 1000

```

---

### all()
 - Returns True if an iterable is either empty or all elements in the iterable are True
 - Equivalent to the following for loop:
 
 ```python
     def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True
```

```python
# simple any 
In [2]: all([False, True])
Out[2]: False

In [3]: all([True, True])
Out[3]: True

In [4]: all([])
Out[4]: True

# any with expression
In [5]: all(role.istitle() for role in ['King', 'Queen', 'Jester'])
Out[5]: True

```

---

### any()
 - Returns True if any of an iterables elements are True, however returns False if the iterable is empty
 - Equivalent to the following for loop:
 
  ```python
     def any(iterable):
        for element in iterable:
            if element:
                return True
        return False
```

```python
In [6]: any([False, True])
Out[6]: True

In [7]: any([False, False])
Out[7]: False

In [8]: any([])
Out[8]: False

In [9]: any(role.istitle() for role in ['King', 'queen', 'jEster'])
Out[9]: True

```

--- 

### ascii()



