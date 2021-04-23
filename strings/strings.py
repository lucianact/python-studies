"""Byte Objects vs String in Python"""

# Byte objects are sequence of Bytes, whereas Strings are sequence of
# characters. Byte objects are in machine readable form internally,
# Strings are only in human readable form. Since Byte objects are 
# machine readable, they can be directly stored on the disk. Whereas, 
# Strings need encoding before which they can be stored on disk.

# "Encondig":
# PNG, JPEG, MP3, WAV, ASCII, UTF-8 are different forms of encodings. 
# An encoding is a format to represent audio, images, text, etc in bytes. 
# Converting Strings to byte objects is termed as encoding. 
# This is necessary so that the text can be stored on disk using mapping
# using ASCII or UTF-8 encoding techniques.

# string:
a = "luciana"

# byte object:
b = b'luciana'

# string to byte
# with enconde
c = a.encode("ascii") 
print(c)

# byte to string
# with decode
d = b.decode("ascii")
print(d)

# using bytes
# with strings
e = bytes(a, "ascii")
print(e)
# with intenger
f = 5
g = bytes(f)
print(g)
# with lists
h = [1, 2, 3]
i = bytes(h)
print(i)


"""String format"""

# old style
name = "luci"
print("Hey %s , hope you're doing wel" % name)

# "new" style
print("Hello {}, sup?".format(name))

# f'strings (python3)
print(f"Hey, {name}! I like this!")

# template strings:
from string import Template
greet = Template('Hi, $name')
print(greet.substitute(name=name))


"""Split method""" 

color = "blue and red"

# without parameters
one = color.split()
print(one)

# with a separator parameter
two = color.split("and")
print(two)

# with a maxsplit parameter:
three = color.split("and", 0)
print(three)


"""Regular Expressions"""

# Regular Expression or RegEx is a sequence of characters that forms a
# search pattern. RegEx is used to search for and replace specific
# patterns. Python provides a built-in module, re, which supports regular 
# expressions.

import re

# re.finall()
phrase = "I have a white cat, she has a blue cat"
print(re.findall("cat", phrase))

# re.search()
# start() -> the start of the index 
print(re.search("cat", phrase).start())

#re.split()
print(re.split(",", phrase))

#re.sub()
print(re.sub("cat", "necklace", phrase))