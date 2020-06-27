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


# .centre(width, [, fillchar])
# If the len of the string is less than width; just return the string.  Otherwise return the centred string
# with the fillchar padding;  by default ASCII space.

>>> default = "default"
>>> default.center(25)
'         default         '

>>> padding = 'padding'
>>> padding.center(25, '*')
'*********padding*********'


#
