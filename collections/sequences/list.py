#  Python lists module is usable for creating ordered sequences of heterogenerous elements.

# Special Notes and mentions:
    """
    - Lists by default are 56 bytes in size
    -

    """

# 1.0 - Creating lists

"""
empty_list = []
empty_list = list()
"""

# 1.1 - Default sizes of lists

"""
As of python 3.8.5 the default bytes size of empty lists are <56 bytes>.  This is accessible through:

>>> from sys import getsizeof as size
>>> size(list())
56
>>> size([])
56
"""