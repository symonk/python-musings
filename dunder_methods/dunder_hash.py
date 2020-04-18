"""
dunder hash (__hash__) is called by the built in hash(obj) function.  Custom implementations should return an integer
The only restriction is that objects deemed to be equal should both return the same integer from hash(obj) as this is
used in certain collections such as set, frozen set and dict.__hash__ (dictionary only supports hashable key value(s).
Having hash implemented allows these containers to do extremely fast accessing and 'in' checks as they do not have to
iterate all items to discover, but instead using hashing.  An advised implementation for __hash__ is to pack
the attributes of the object into a tuple and hash the result
"""


class PreferredHash:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


pref = PreferredHash(100, 'test')
print(hash(pref))

"""
Results in:

-2120064241806105461


So what does this buy us? well it allows for storing such items as dict keys, into sets etc, lets have a look at that:
"""


class NoHash:
    pass

a = NoHash()
b = NoHash()
print(a is b)
my_set = {NoHash(), NoHash()}
print(my_set)

"""
Results in:

False
{<__main__.NoHash object at 0x00000228A5D31860>, <__main__.NoHash object at 0x00000228A5D317F0>}

As you can see, by default python sets do not allow duplicates, so why is there 2 NoHash instance pointers there?
Well, thats because by default the NoHash classes are not considered duplicates, they are not equals.  Lets try implement
only a __hash__

"""


class OnlyHash:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))


one = OnlyHash(10, 20)
two = OnlyHash(10, 20)
three = OnlyHash(20, 30)
new_set = {one, two, three}
print(new_set)

"""
Results in:

{<__main__.OnlyHash object at 0x000001DC0FD719B0>, <__main__.OnlyHash object at 0x000001DC0FD71A20>, <__main__.OnlyHash object at 0x000001DC0FD719E8>}

What the? but all 3 are still stored! This should only be two references, one and two are the same!
Are they? this also requires __eq__ implement to solve

"""

print('-----')
print(one == two) #


class HashAndEq:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return other.x == self.x and other.y == self.y


print('----')
one = HashAndEq(1, 2)
two = HashAndEq(1, 2)
three = HashAndEq(3,4)

print(one == two)
print(two == three)

# That looks a bit better, now our set

my_set = {one, two, three} # should be one and three here, as 2 is a duplicate!
print(my_set)

"""
Results in:
----

True
False
{<__main__.HashAndEq object at 0x000002217B181B38>, <__main__.HashAndEq object at 0x000002217B181BA8>}

"""
