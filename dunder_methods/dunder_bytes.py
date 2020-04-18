"""
dunder bytes (__bytes__) is used to return a byte-string representation of an object.  The contract of this method
is that it should return a bytes object <class 'bytes'>.  Bytes objects are immutable sequence of integers ranging from
0-256.  bytes are immutable versions of the (mutable) bytearray.  Bytes objects can be created by prefixing strings for
example with a 'b'.  Anything stored on a computer (on disk) must be encoded, computers are only really capable of
storing 'bytes'.

What is a byte? a sequence of 8 bit unsigned values
"""

my_bytes = b'Hello'
print(my_bytes)
print(type(my_bytes))
to_string = my_bytes.decode(encoding='utf-8')
print(to_string)
back_to_bytes = to_string.encode()
print(back_to_bytes)

my_bytes2 = b'hello'
print(list(my_bytes2))
print([type(x) for x in my_bytes2])

print(bytes(100))

"""
Results in:

b'Hello'
<class 'bytes'>
Hello
b'Hello'
[104, 101, 108, 108, 111]
[<class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>]
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

"""

