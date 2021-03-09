# 1
# Bubble Sort:
# takes an unsorted list and orders it in ascending values
# lowest number will be in the beginning of the list
# highest number will be in the end
# we do that by comparing two side by side values

def bubble_sort(lst):
    """Bubble the highest number to the end"""

    # nested for loop reminder:
    # the "inner loop" will be executed one time
    # for each iteration of the "outer loop"
    for i in range(len(lst) - 1):
        made_swap = False
        # if we want to make it shorter, replace 
        # [for j in range(len(lst) - 1)] for:
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True
        if not made_swap:
            break

    return lst

lst = [6, 4, 8, 3, 2, 5, 7, 8, 9]
print(bubble_sort(lst))

# # 2
# # Merge Sort O(n log n):
# # divide and conquer
# # reducing lists to 0-1 list items
# # then recomnining them

# def merge_sort(lst):
#     if len(lst) > 1:
#         mid = len(lst) // 2
        



