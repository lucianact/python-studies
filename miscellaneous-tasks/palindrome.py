# 1
# Convert a list of characters into a string:
# Input  -> chars = ["l", "u", "c", "i", "a", "n", "a"]
# Output -> "luciana"

# Method 1:
# traveral of a list
def convert_to_string(chars):
    to_string = ""
    for char in chars:
        to_string += char
    return to_string

chars = ["l", "u", "c", "i", "a", "n", "a"]
print(convert_to_string(chars))

# Method 2:
# using join() function
def convert_to_string_using_join(chars2):
    return "".join(chars)

chars2 = ["l", "u", "c", "i", "a", "n", "a"]
print(convert_to_string_using_join(chars2))

# 2
# while loop
# what's the effect of the break statement?
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# what's the effect of the continue statement?
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
