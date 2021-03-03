# Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.

# To do this, you’ll need to know when any team is having a meeting. 
# In HiCal, a meeting is stored as a tuple of integers:
# (start_time, end_time)
# These integers represent the number of 30-minute blocks past 9:00am.

# For example:
# (2, 3)  # Meeting from 10:00 – 10:30 am
# (6, 9)  # Meeting from 12:00 – 1:30 pm

# Write a function merge_ranges() 
# that takes a list of multiple meeting time ranges 
# and returns a list of condensed ranges.

# def merge_ranges(meetings):
#     sorted_meetings = sorted(meetings)
#     print(sorted_meetings)
#     condensed_meetings = []
#     start_index = 0
#     while start_index < (len(sorted_meetings) - 1):
#         if (sorted_meetings[start_index][1] == sorted_meetings[start_index+1][0]) or (sorted_meetings[start_index][1] > sorted_meetings[start_index+1][0]):
#             new_tuple = (sorted_meetings[start_index][0],sorted_meetings[start_index+1][1])
#             condensed_meetings.append(new_tuple)
#             sorted_meetings.pop(start_index+1)
#         else:
#             condensed_meetings.append(sorted_meetings[start_index])
#         start_index += 1
#     return condensed_meetings

def merge_ranges(meetings):

    # Sort by start time
    # (list of tuples)
    sorted_meetings = sorted(meetings)
    # print(sorted_meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    # print(merged_meetings)

    # Compare the start and end time of next meetings with previous meeting:
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                max(last_merged_meeting_end,
                                    current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]
print(merge_ranges(meetings))

# Write a function that takes a list of characters 
# and reverses the letters in place:

# Note: not askinf to reverse in sorted/lexicographic order! 

def reverse_chars(list_of_chars):

    left_index = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:

        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1
    
    return(list_of_chars)

list_of_chars = ["n", "i", "c", "o"]
print(reverse_chars(list_of_chars))

# Write a function reverse_words() that takes a message 
# as a list of characters and reverses 
# the order of the words in place

def reverse_words(message):
   
    string_message = "".join(message).split(" ")
    print(string_message)

    final_output = reverse_chars(string_message)
    print(final_output)

    return " ".join(final_output)

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

print(reverse_words(message))

# We have our lists of orders sorted numerically already, in lists. 
# Write a function to merge our lists of orders into one sorted list.

def merge_lists(my_list, alices_list):
    # return sorted(arr1 + arr2)

    # Make a list big enough to fit the elements from both lists
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size
    print(merged_list)

    head_of_my_list = my_list[0]
    head_of_alices_list = alices_list[0]

    if head_of_my_list < head_of_alices_list:
        # Case: 0th comes from my list
        merged_list[0] = head_of_my_list
    else:
        # Case: 0th comes from Alice's list
        merged_list[0] = head_of_alices_list

    # Eventually we'll want to return the merged list
    return merged_list


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(merge_lists(my_list, alices_list))