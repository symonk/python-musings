"""
Part of the python iterator protocol, dunder __iter__ is invoked by the built in when attempting to return an
`iterable` from an `iterator`.  These terms are often confusing and are outlined below:

-> `iterable` something which when called by the built in iter(obj) returns a fresh iterator instance.
-> `iterator` something which can be sequentially iterated over.

Note: An object can also implement dunder __getitem__ in order to be considered iterable.  One caveat of this is
that the object itself needs to support iteration via a 0-based integer incrementation method:

Note: When checking if something is iterable, doing a subclass check on Iterable is not enough because this does
NOT account for the old style iteration support via __getitem__.  The simplest method is to iter(obj) and catch the
type error to determine obj x is NOT iterable.

Note: An iterable should always return a fresh iterator each time it is called, to avoid weird exhaustion issues,
side effects and subtle defects.

Note: Iterables & Iterators are often confused;  Making your custom iterable also its own iterator (response for next)
is a very bad idea.  Iterators are iterable; but iterables are NOT iterators.  It pays well to remember this & the
caveat to why this exists is outlined below.

Note: ??? Virtual subclassing explained regarding __iter__ etc.

Note: ??? Free __iter__ if you subclass abc.Iterator

__getitem__(self, key=0); __getitem__(self, key=1); __getitem__(self, key=n)... & so fourth.

"""
import re
from typing import Iterable


WORDS_RE = re.compile(r"\w+")


class Sentence:
    def __init__(self, text: str):
        """
        A simple sentence class, that permits iterating over the space separated text it was provided.
        :param text: A string of text to parse into words.
        """
        self.words = WORDS_RE.findall(text)

    def __getitem__(self, key: int):
        """
        This dunder __getitem__ implementation actually permits the Sentence class being considered `iterable`.
        :param key: The key to lookup, an integer used for [key] lookups.
        """
        return self.words[key]


def is_sentence_iterable():
    se = Sentence("how now brown cow")
    print(issubclass(Sentence, Iterable))  # False
    print(isinstance(se, Iterable))  # False
    # Both these checks return False; surely we cannot iterate over the sentence class instances?
    for word in se:
        # As you can see, this actually works, even tho the previous checks failed.
        # This is due to __getitem__ being called as a backup
        # Note: This only works if your instance supports integer 0-based incremental lookup!
        print(word)  # how now brown cow


def true_sentence_iterability():
    """
    A simple method of checking for iterability, is to create an iterator out of the object.
    A TypeError is raised by python in the event of such fail; catch it and return a boolean.
    """
    se = Sentence("how now brown cow")
    print(_is_obj_iterable(se))  # True
    print(_is_obj_iterable(Sentence))  # False?


class NewStyleSentence:
    """
    A simple new style sentence class that uses the dunder __iter__ implementation.
    Remember; an iterable is something that when invoked by iter(x) returns an Iterator.
    Note to be confused by Iterator(which themselves are often iterable), but they implement __next__ too!
    """
    def __init__(self, text: str) -> None:
        self.words = WORDS_RE.findall(text)

    def __iter__(self):
        # Dunder __iter__ implementations should always return a fresh iterator to avoid subtle defects.
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        # If you inherit from collections.abc.Iterator a concrete implementation of this exists already.
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


class CoupledSentence:
    """
    This coupled class is often an anti pattern when people are creating their own
    iterables & iterators.  To be clear; iterables have a dunder __iter__ implementation
    and iterators have both a dunder __iter__ and a __next__ implementation, most of the time
    their dunder __iter__ just returns self.  This in a nutshell is what makes iterators
    by design iterable themselves.

    The problem arises here that it may be tempting to bundle your class like outlined below.
    @see: `a_coupled_sentence()`

    """
    def __init__(self, text: str) -> None:
        self.words = WORDS_RE.findall(text)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


class AGeneratorSentence:
    def __init__(self, text: str):
        self.words = WORDS_RE.findall(text)

    def __iter__(self):
        # here we return a generator function, no separate Iterator class is necessary now...
        for word in self.words:
            yield word


def _is_obj_iterable(obj) -> bool:
    try:
        _ = iter(obj)
        return True
    except TypeError:
        return False


def dunder_iter_sentence():
    se = NewStyleSentence("one two three four")
    for word in se:
        # one; two; three; four
        print(word)


def generators_to_the_rescue():
    for _ in range(10):
        for word in AGeneratorSentence("example words here"):
            # Prints example words sentence, 10 times.
            # Note: The iterator is not exhausted and continues to return values!
            print(word)


def a_coupled_sentence():
    coupled_se = CoupledSentence("my sentence class is coupled")
    print("-----")
    for word in coupled_se:
        print(word)  # Fine, looks great.
    for word_again in coupled_se:
        print(word_again)  # Wait, there was nothing left to iterate over, it was exhausted by attempt #1 above.


if __name__ == '__main__':
    is_sentence_iterable()
    true_sentence_iterability()
    dunder_iter_sentence()
    a_coupled_sentence()
    generators_to_the_rescue()