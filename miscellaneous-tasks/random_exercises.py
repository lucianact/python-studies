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


# 4
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, 
# so all numbers are in the range [0,3]. 2 is the missing number 
# in the range since it does not appear in nums.
# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, 
# so all numbers are in the range [0,2]. 
# 2 is the missing number in the range since 
# it does not appear in nums.
# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, 
# so all numbers are in the range [0,9]. 
# 8 is the missing number in the range since 
# it does not appear in nums.
# Example 4:
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, 
# so all numbers are in the range [0,1].
# 1 is the missing number in the range 
# since it does not appear in nums.
 
# Constraints:
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

def missingNumber(nums):
    
    n = len(nums)
    print(n)
    
    sum1 = 0
    for i in range(n+1):
        sum1 += i 
    print(sum1)
    
    sum2 = 0
    for num in nums:
        sum2 += num
    print(sum2)
    
    value = sum1 - sum2
    print(value)
    
    return value 
    
    # checking the len of array
    # -> 9 
    # sum nums range (0-9)
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
    # sum of n - sum of num = missing number 

print(missingNumber([9,6,4,2,3,5,7,0,1])) 