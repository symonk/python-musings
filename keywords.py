# The 'import' keyword is used to import python modules into the current namespace
# If you want to be specific and import specific attributes or functions we can use import ... from ...
import keyword
from math import cos

print(keyword.kwlist)
print(cos(25))

-------------------------------------------------------------------------------------------------------------

# The 'as' keyword can be used to give an import a customised name for reference within our module
from math import cos as alias

alias(25)

-------------------------------------------------------------------------------------------------------------

# 'True' and 'False' are typical Truth values in python, like pretty much anything

1 == 1 #True
5 == 4 #False
True and False #False

-------------------------------------------------------------------------------------------------------------

# 'None' is the absence of a value or a 'null' value from other languages
#  not returning anything from a method, automatically returns None in python
#  care advised because
None == 0 # False
None == [] # False
None == False # False
x = None
y = None
x == y # True

-------------------------------------------------------------------------------------------------------------

# 'and', 'or', 'not' are the logical operators in python
# 'and' truth table: ('and' results in True only if both operators are True)

a = True, b = True, : a and b # True
a = False, b = True : a and b # False
a = True, b = False : a and b # False
a = False, b = False : a and b # False (*careful here)

# 'or' truth table: ('or' results in True if any of the operators are True)
a = True, b = False : a or b # True
a = False, b = True : a or b # True
a = False, b = False : a or b # False
a = True, b  = True : a or b # True

# 'not' truth table: ('not' flips the result, similar to '!' in java
a = True : a not True # False
a = False : a not True # True

1 == 1 and 5 == 5 # True
1 == 2 or 2 == 2 # True
1 == 3 or 2 == 5 # False
not False # True

-------------------------------------------------------------------------------------------------------------

# 'assert' keyword is primarily used for debugging / testing
# if the assertion resolves to True nothing happens, else an AssertionError is raised
a = 10
assert a > 25 # AssertionError
assert a < 15 # Nothing

# We can also provide a message to the assertion error:
assert a > 25, "Error: a is not greater than 25!"

# 'assert' can be thought of as this:
if not condition:
    raise AssertionError(message)

-------------------------------------------------------------------------------------------------------------

# 'break' like most languages is used to break out of the most innerloop
# 'continue' like most languages is used to break out and enter the next loop iteration
# switch-case statements don't seem to exist in python

# 'break' in action:
for i in range(10):
    if i == 5:
        break
    print(i)

# results in => '1,2,3,4' printed to console and the loop completely terminated

# 'continue' in action:
for i in range(15):
    if i % 3 == 0:
        continue
    print(i)

# results in => '1,2,4,5,7,8,10,11,13,14 printed to console and the loop skipping the print on divisible by 3 numbers

-------------------------------------------------------------------------------------------------------------

# 'class' is used to define a new user-defined class in python
# classes like any language are used to achieve OOP, they consist of instance variables (state) and methods (behaviour)
# they can also contain static / class vars and methods, we will discuss more on that later.
# it is good practice when not extending a class to explicitly extend object (like most OOP languages do implicitly)

class SimonClass(object):

-------------------------------------------------------------------------------------------------------------

# 'def' is used to declare a new function (define if you will)
# here we define a function called 'do_something' that multiplies two numbers and returns their value

def do_something(self, first : int, second : int = 5) -> int:
    result = first * second
    print(result)
    return result

-------------------------------------------------------------------------------------------------------------

# 'del' is a surprisingly one if you come from a static typed language like java
# everything in python is an object, everything.  del is used to delete a reference to an object
this_value_will_be_deleted = 10
print(this_value_will_be_deleted) # prints 10
del this_value_will_be_deleted # ?? weird
print(this_value_will_be_deleted) # error

Traceback (most recent call last):
  File "<stdin>", line 1, in <module
NameError: name 'this_value_will_be_deleted' is not defined

-------------------------------------------------------------------------------------------------------------

