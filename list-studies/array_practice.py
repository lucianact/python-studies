# 1
# # Write a function merge_ranges() 
# that takes a list of multiple meeting time ranges 
# and returns a list of condensed ranges.
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

# meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]
# print(merge_ranges(meetings))

# 2
# Write a function that takes a list of characters 
# and reverses the letters in place:
# Note: not asking to reverse in sorted/lexicographic order! 
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

# list_of_chars = ["n", "i", "c", "o"]
# print(reverse_chars(list_of_chars))

# 3
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

# print(reverse_words(message))

# 4
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

# print(merge_lists(my_list, alices_list))

# 5
# Write a function to check that my service is first-come, first-served. 
# All food should come out in the same order customers requested it.
# We'll represent each customer order as a unique integer.
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if (take_out_orders_index <= take_out_orders_max_index and 
                order == take_out_orders[take_out_orders_index]):
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif (dine_in_orders_index <= dine_in_orders_max_index 
                and order == dine_in_orders[dine_in_orders_index]):
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if (dine_in_orders_index != len(dine_in_orders) or
        take_out_orders_index != len(take_out_orders)):
        return False


    if served_orders == []:
        return False

    elif take_out_orders == [] or dine_in_orders == []:
        if take_out_orders != served_orders or dine_in_orders != served orders:
            return False

    elif take_out_orders[0] == served_orders[0] or dine_in_orders[0] == served_orders[0]:

    take_out_orders_index = 0
    dine_in_orders_index = 0
    served_orders_index = 0

        while take_out_orders_index or dine_in_orders_index <= len(served_orders) - 1:

            if take_out_orders[take_out_orders_index] == served_orders[served_orders_index]:
            take_out_orders_index += 1
            served_orders_index += 1

            elif dine_in_orders[dine_in_orders_index] == served_orders[served_orders_index]:
            dine_in_orders_index += 1
            take_out_orders_index +1
        
            else:
                return False
        
        return True 
