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

# 'and', 'or', 'not' are the logical operators in python and will result in true if both operands are true
# see truth tables for each below:

a = True, b = True, => a and b # True
a = False, b = True => a and b # False
a = True, b = False => a and b # False
a = False, b = False => a and b # False (*careful here)
