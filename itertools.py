import string

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
    def __init__(self) -> None:
        self.flavour = "salted"





# Infinite Iterators

"""
Infinite Iterators:

    Computing infinite numbers has a memory consumption problem, often when generating a simple
    list you do not need to think about the memory footprint of such list.
    
    Problem statement: You work for the 
"""