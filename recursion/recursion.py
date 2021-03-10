
# Review:
# understanding a call stack
def a():
    print("hello")
    b()
    print("python")

def b():
    print("word")
    c()
    print("love")

def c():
    print("i")

a()
# when you call a function, you "freeze" where you are
# until the function returns something and then,
# it continue where you left off

# Recursion vs loops:
def count_recursive(n):
    """Count to 3, using recursion."""
    if n > 3:
        return
    print(n)
    count_recursive(n + 1)

n = 1
count_recursive(n)
# every recursion needs a base 
# (usually a "degenerate case")
# so we know when "we're done"

# Task:
# return length of list using recursion without using len()
def len_of_lst(lst):
    if not lst:
        return 0
    print(lst)
    return 1 + len_of_lst(lst[1:])

print(len_of_lst(['apple', 'berry', 'cherry']))

# for every item in a list, print the value, doubled
def doubler_recursive(lst):
    for n in lst:
        if isinstance(n, list):
            doubler_recursive(n)
        else:
            print(n * 2)


doubler_recursive([ 1, [2, 3], 4 ])

# print items in list doubled, using recursion but no loop
def doubler_no_loop(lst):
    if not lst:
        return

    n, rest = lst[0], lst[1:]

    if isinstance(n, list):
        doubler_no_loop(n)
    else:
        print(n * 2)

    doubler_no_loop(rest)

doubler_no_loop([ 1, [2, 3], 4 ])
