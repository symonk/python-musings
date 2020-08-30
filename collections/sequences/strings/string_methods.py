"""
>>> from pprint import pprint
>>> methods = [x for x in dir('')]
>>> pprint(methods)
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isascii',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']
"""


def capitalize() -> str:
    # Return a copy of the string with its first letter capitalized.
    # args: None
    # note: for 8-bit strings, this method is locale dependent.
    # note: As of python 3.8, this applies 'title' casing to the first letter (better support for digraphs etc).
    """
    >>> 'hello world example'.capitalize()
    'Hello world example'
    """


def casefold() -> str:
    # Returns a copy of the string with more 'aggressive' lower() application
    # args: None
    # note: The case folding algorithm is described in section 3.13 of the unicode standard
    """
    >> > german = "ßest"
    >> > german.lower()
    'ßest'
    >> > german.casefold()
    'ssest'
    """
    ...


def center() -> str:
    # Return a copy of the string centered in a string of length (width) (Padded by fillchar)
    # args: width(required), fillchar(optional)
    # note: default ascii filler character is a blank space.
    # note: fillchar must be exactly 1 ASCII character
    """
    >>> word = 'hello'
    >>> word.center(20)
    '       hello        '
    >>> word.center(20, '*')
    '*******hello********'
    >>>
    """
    ...


def count() -> int:
    # Returns the total of non overlapping occurrences of a substring
    # args: sub(required), start(optional - interpreted as slice notation), end(optional - interpreted as slice notation)
    """
    >>> word = 'eggbaconsausageeggs'
    >>> word.count('egg')
    2
    >>> word.count('egg', 10)
    1
    >>> word.count('egg', 10, 15)
    0
    >>> print(word[10:15])
    usage
    >>>
    """
    ...


def encode() -> bytes:
    # Returns the encoded string object as bytes.
    # args: encoding('utf-8' - optional), errors('strict' - optional).
    # note: error= can be passed a different error handling scheme.
    # note: by default UnicodeErrors are raised if encoding fails ('strict').
    # note: other options are ('ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'.
    # note: custom error handles can be registered via the codecs.register_error() function.
    # note: see (https://docs.python.org/3/library/codecs.html#standard-encodings) for standard encodings list.
    # note: Keyword args supported as of python 3.1
    """

    """
    ...