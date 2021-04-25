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

# 3 
# How would you sort a dictionary in Python?

# dict = {"key" : "value"}
# unordered 
# dict.sorted()
# ->  sorted(dict)

# should I modify the dict or
# just return its values, keys or items sorted
# with a different type of data 
dic = {"b" : "nico", "a" : "luci"}
sorted_dict = sorted(dic.items()) 
print(sorted_dict)
print(dic)
# list of tuples
# tuple[0] -> key
# tuple[1] -> value
new_dict = {} 
for pair in sorted_dict:
    new_dict[pair[0]] = pair[1]

print(new_dict)
# does that mean you cannot sorte a 
# dict in place? 


# should I sorted dict its values or keys? 
# => keys 
# loop through the keys of the dict
# check all the keys 
# to be able to sort the key-value pair
# This is not a good idea