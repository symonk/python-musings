from __future__ import annotations

import random
import string
from typing import Iterable, Any

"""
The itertools module exposes a number of iterator building blocks.  The exposed functions
are very memory efficient, fast and are extremely useful alone, or as a combination with
others.
"""

# What exactly is an Iterable and an iterable in python?

    # iter() built in
    # dunder __iter__
    # Iterables can be Iterators etc


"""
Where it all begins, the python `for in` loop; not to be confused with a traditional for loop
if you are familiar with other languages.
"""
def for_in_loop() -> None:
    """
    Given something `iterable`, python can loop through it one element at a time.
    We will talk more about the definition of iterables later throughout this
    document, but have a look at the below trivial example.
    :return: None

    Pseudo code of the function:
        -> Create a reference to the lower case ascii string.
        -> Strings in python are `iterable` as they are considered a Sequence.
        -> Each iteration, grab the next character in the string and print it.
    """
    letters = string.ascii_lowercase
    for character in letters:
        print(character)


"""
After understanding the simple `for in` loop concept in python, you need to then
look closer at the data object model, namely:
    - Dunder iter -> `__iter__`
    - Dunder next -> `__next__`
    
These dunder functions are known as the building blocks of the new Iterator protocol.
Something we will discuss later is the older style iterator protocol for sequences etc.
But for now, just understand that objects implementing dunder `__iter__` and dunder
`__next__` are supported out of the box by `for in` loops.  To demonstrate a basic
example of this, we will write our own custom implementation of a infinite packet
of crisps, all you eat, so to speak, with a twist - you never know what flavour
of crisp you are going to get next! but it's all you can eat regardless.
outlined below:
"""
class CrispPacket:
    flavours = ("beef", "cheese and onion", "salt and vinegar", "steak")

    def __iter__(self) -> CrispPacketIterator:
        return CrispPacketIterator(self)


class CrispPacketIterator:

    def __init__(self, source: CrispPacket) -> None:
        self.source = source

    def __next__(self) -> str:
        return random.choice(self.source.flavours)


def the_hello_world_of_iterators() -> None:
    """
    Here we will instantiate an instance of our CrispPacket
    and use it with a for in loop.  This will create a
    randomised indefinite output to stdout:
        cheese and onion
        cheese and onion
        steak
        cheese and onion
        salt and vinegar
        beef
        salt and vinegar
        salt and vinegar
        cheese and onion
        ... and so on and so fourth, indefinitely
    :return: None
    """
    for flavour in CrispPacket():
        print(flavour)


"""
That's great, but still confusing to look at, lets understand how for in loops actually function in python.
To break down the `for in` for our example (infinite and printing), similar code is outlined below:
"""

def infinite_printing_for_in(obj: Any) -> None:
    """
    Given an object, get an iterator for the object using the built in iter function.
    Under the hood this invokes dunder __iter__ on custom objects, returning an iterator
    while True (loop forever), fetch the next item from the iterator by using the
    built in next() function, which under the hood invokes dunder __next__ on the iterator.
    :param obj: Any object implementing the iterator protocol
    :return: None
    """
    it = iter(obj)
    while True:
        print(next(it))


"""
And here in lies the first benefit of iterators (and the itertools building blocks) to recreate
something like our example in a simple python list is technically impossible, memory will
eventually be exhausted, there is no way to store infinite values in a list, this is what makes
iterators and iterables a fantastic concept, with some very powerful use cases.  Think of them
for now as objects that promote lazy/deferred iteration.

You have probably pondered, why the need for multiple classes here?  Combining them into one class
is completely possible and advisable, however there is a caveat that we will discuss soon.  For now
just understand that the Iterator protocol only cares that whatever is returned by the objects
dunder __iter__ has an implementation of dunder __new__.  While thinking about this keep in the 
back of your mind that everytime we iterate over an iterable, it should be a fresh, this is where
people often make mistakes.

Lets simplify our CrispPacket class by making it implement both protocol methods and bin the 
concept of a CrispPacketIterator class.
"""

class ImprovedCrispPacket:
    flavours = ("beef", "cheese and onion", "salt and vinegar", "steak")

    def __iter__(self) -> ImprovedCrispPacket:
        return self

    def __next__(self) -> str:
        return random.choice(self.flavours)


"""
Pretty successful, we have removed the need for an isolated Iterator class, returning
self from iter guarantees that we are returning an object which implements dunder next.
clean, concise and understandable.  This highlights a key fact:

    -> All Iterators are iterables
    -> Not all Iterables, are Iterators
    
Implementing it the long winded way to begin with, helps to grasp the concepts under the 
hood and expected contract of the iterator protocol.

Moving on to more realistic iterator examples, because who wants to iterate forever
really? The use case is pretty small.

You are probably pondering (again) how can we signal when an iterator is exhausted
and should stop returning values and the answer to that is quite unique, it all
boils down to the `StopIteration` exception which is used to signal the end.

Using the python built ins we can easily see what is going on under the hood:
"""

def built_in_iter() -> None:
    x = iter(range(3))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))

"""
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-4-a2816fdfbc1a> in <module>
----> 1 built()

<ipython-input-3-5afbb6d48dee> in built_in_iter()
      4     print(next(x))
      5     print(next(x))
----> 6     print(next(x))
      7

StopIteration:

"""


class BoundedIterable:
    def __init__(self, attempts):
        self.attempts = attempts
        self.tally = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.tally == self.attempts:
            raise StopIteration
        self.tally += 1
        return self.tally

"""
Let's try out our BoundedIterable, based on the number of attempts we pass into
its constructor,
"""

def bounded():
    attempts = 3
    it = iter(BoundedIterable(attempts))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

"""
bounded()
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-17-f6e8ae88637a> in <module>
----> 1 bounded()

<ipython-input-16-e16e1a260943> in bounded()
      5     print(next(it))
      6     print(next(it))
----> 7     print(next(it))
      8

<ipython-input-9-377374344e41> in __next__(self)
      9     def __next__(self):
     10         if self.tally > self.attempts:
---> 11             raise StopIteration
     12         self.tally += 1
     13         return self.tally

StopIteration:

"""


# Infinite Iterators

"""
Infinite Iterators:

    Computing infinite numbers has a memory consumption problem, often when generating a simple
    list you do not need to think about the memory footprint of such list.
    
    Problem statement: You work for the 
"""