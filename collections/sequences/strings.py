# Strings in python are immutable sequences of unicode code characters.

# .capitalize()
# Return a copy (immutable strings) of the string in capitilized form (initial letter capitilized) and the
# rest lower cased.  This has been changed in python 3.8 to return the title() equivalent on the first character.

>>> word = 'word'
>>> word.capitalize()
'Word'


# .casefold()
# Return a copy (immutable strings) of the string in casefold.  These may be useful for caseless matching.
# Case folding is a more aggressive form of lowercasing

>>> already_lower = 'ß'
>>> already_lower.lower()
'ß'
>>> already_lower.casefold()
'ss'


# .center(width, [, fillchar])
# If the len of the string is less than width; just return the string.  Otherwise return the centred string
# with the fillchar padding;  by default ASCII space.

>>> default = "default"
>>> default.center(25)
'         default         '

>>> padding = 'padding'
>>> padding.center(25, '*')
'*********padding*********'


#  .count(substring[, start[, end]])
# returns the number of non overlapping substrings found in the string in the given range
# optional args start, end are interpreted as slice notation
>>> words = 'one two three one two three onesie'
>>> words.count('one')
3
>>> words.count('one', 0, 4)
1

