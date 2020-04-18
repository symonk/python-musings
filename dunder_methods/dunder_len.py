"""
By default, custom classes do not support the dunder len method, and thus cannot avail of the builtin
len() function.  This is outline below:
"""


class LenClass:
    def __init__(self):
        print('My custom class')


len(LenClass())

"""
This results in:

Traceback (most recent call last):
  File "C:/workspace/learning-python/dunder_methods/dunder_len.py", line 12, in <module>
    len(CustomClazz())
TypeError: object of type 'CustomClazz' has no len()

Process finished with exit code 1
"""

"""
Implementing len() is relatively straight forward, the function should return an integer
"""


class ImprovedLenClass:
    def __init__(self):
        print('new and improved!')

    def __len__(self):
        return 10


print([x for x in range(len(ImprovedLenClass()))])

"""
new and improved!
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
