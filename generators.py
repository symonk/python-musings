"""
Python generators return a lazy iterater, by that we mean that value is only computed on a per loop basis.  The
main advantage to this is that memory footprint is drastically reduced.  Lets say in a basic example you have a
windows 1995 system and 1GB of memory, but you are forced into dealing with a large data set.  This problem can be solved
by the use of generators as outlined below:
"""
import sys


def non_gen():
    # memory footprint here is pretty huge....
    return [x for x in range(10000)]


items = non_gen()
print(f"memory footprint of list: {sys.getsizeof(items) / 1048576 } megabytes")


"""
Results in:

memory footprint of list: 0.08356475830078125 megabytes
wow, nearly 820Mb of memory consumed...
Lets have a look at a 'lazy' generator iterator:
"""


def gen():
    for x in range(10000):
        yield x


items2 = gen()
print(type(items2))
print(f"memory footprint of list: {sys.getsizeof(items2) / 1048576 } megabytes")

"""
Results in:

<class 'generator'>
memory footprint of list: 0.00012969970703125 megabytes (hardly anything...)

In order to iterate over the generator, we keep invoking next(gen) until it interally raises a StopIteration
in which python uses as a flow of control to terminate, Lets see what that looks like:
"""

for item in items:
    print(item)  # List way; fine!


print('-----')

for item in items:
    print(item)  # Gen way; only 1 value at a time!
    #  will break out of the while loop, because a StopIteration will be raised


"""
We can check if a function is considered a generator (yields atleast once in its body) using the inspect or dir 
modules.  This is demonstrated below
"""


def mygen():
    yield 20
    yield 30


def nogen():
    return 10


import inspect

print('-----')
print(inspect.isgeneratorfunction(mygen))
print(inspect.isgeneratorfunction(nogen))


import dis

print('-----')
print(dis.dis(mygen))


"""
-----
True
False
-----
 65           0 LOAD_CONST               1 (20)
              2 YIELD_VALUE
              4 POP_TOP

 66           6 LOAD_CONST               2 (30)
              8 YIELD_VALUE
             10 POP_TOP
             12 LOAD_CONST               0 (None)
             14 RETURN_VALUE
None

Process finished with exit code 0


"""


""""
A closer look at generator functions and their methods, dir() of a generator function will yield the following:


>>> items = [item for item in dir(gen()) if '__' not in item]
>>> print(sorted(items))
['close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']

"""


def gen():
    yield 100


# generator.close()
# The purpose of gen.close() is to raise a GeneratorExit inside a generator.

print(help(gen()))


# all gen functions with examples


# type hinting a generator [None, None, None etc]


#
