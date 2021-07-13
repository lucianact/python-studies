# Well, how would we check that a string is a palindrome?
#  We could use the somewhat-common "keep two pointers" pattern. 
# We'd start a pointer at the beginning of the string and a pointer 
# at the end of the string, and check that the characters at those pointers
# are equal as we walk both pointers towards the middle of the string.

def isPalindrome_1(s):
    return s == s[::-1]

def isPalindrome_2(str):
    # let suppose str = civic
    middle = int(len(str)/2)
    # /2 will "floor down" if necessary 
    print(middle) 
    # right now middle is 2
    
    for i in range(0, middle):
        # range will start does not include the second argument int 
        # pseudo code:
        # for i in range (0, 10):
        # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        if str[i] != str[len(str)-i-1]:
            # breaking it down:
            # c != 5-0-1 => 4 => c
            # i = 5-1-1 => 3 => i 
            return False
    return True

def isPanlidrome_3(str):

    # let suppose str = civic
    print(str)
    # civic

    middle = int(len(str)/2)
    print(middle)
    # 2

    first_part = str[:middle]
    print(first_part)
    # first_part = ci
    len_first_part = len(first_part)
    # 2

    second_part = str[middle:]
    print(second_part)
    # second_part = vic
    
    first_index = 0
    second_index = -1
    
    while True:
        if first_index == len_first_part:
            # len(first_part) will be smaller than len(second_part) if len(str) is odd 
            break
        if first_part[first_index] == second_part[second_index]:
            # first_index = 0
            # second_index = -1 
            # c == c 
            # first_index = 1
            # second_index = -2 
            # i == i
            first_index += 1
            second_index -= 1
        else:
            False
    
    return True

# How can we tell if any permutation of a string is a palindrome?
# Our approach is to check that each character appears an even number of times, 
# allowing for only one character to appear an odd number of times (a middle character). 
# This is enough to determine if a permutation of the input string is a palindrome.

# We iterate through each character in the input string, keeping track of the characters 
# we’ve seen an odd number of times using a set unpaired_characters.
# As we iterate through the characters in the input string:
# If the character is not in unpaired_characters, we add it.
# If the character is already in unpaired_characters, we remove it.
# Finally, we just need to check if less than two characters don’t have a pair.
def has_palindrome_permutation(the_string):

    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else: 
            unpaired_characters.add(char)
    
    if len(unpaired_characters) <= 1:
        return True 

print(has_palindrome_permutation("ccivi"))