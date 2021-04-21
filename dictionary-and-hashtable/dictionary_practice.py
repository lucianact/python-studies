"""
Write a function that takes an integer flight_length (in minutes)
and a list of integers movie_lengths (in minutes) and 
returns a boolean indicating whether there are two numbers in 
movie_lengths whose sum equals flight_length.

When building your function:
- Assume your users will watch exactly two movies
- Don't make your users watch the same movie twice
- Optimize for runtime over memory

"""
def can_two_movies_fill_flight(movie_lengths, flight_length):
    """ Determine if two movie runtimes add up to the flight length."""

# to find two movies whose sum are smaller or same as the 
# flight length, we would have to iterate through this list
# a couple of times - which isn't great for time cost.

# suppose the flight is 600 minutes
# and we have this follwing list:
# [300, 400, 500, 600, 200]
# this is one way of tackling this problem:
    if len(movie_lengths) <= 1:
        return False

    first_el = movie_lengths[0]
    print(first_el)
    movie_lengths = movie_lengths[1:]
    print(movie_lengths)
    sums = []

    while True:
        for i in range(len(movie_lengths)):
            sum = first_el + movie_lengths[i]
            print(sum)
            sums.append(sum)
        first_el = movie_lengths[0]
        print(first_el)
        movie_lengths = movie_lengths[1:]
        print(movie_lengths)
        if movie_lengths == []:
            break

    print(sums)
    for sum in sums:
        if sum <= flight_length:
            return True

    return False

print(can_two_movies_fill_flight([300, 400, 500, 600, 200], 600))
# but time cost would be not great in this case! O(n*n)

# here's a better way of tackling it with O(n)
def can_two_movies_fill_flight_2(movie_lengths, flight_length):

    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False       
    return False

"""    
Write an efficient function that checks whether any permutation of
an input string is a palindrome.
You can assume the input string only contains lowercase letters.

"""
def has_palindrome_permutation(the_string):
    """Check if ANY permutation of the input is a palindrome."""

    # suppose we have this string:
    # civic 
    # one of its permutation is also civic

    # how can we check strings permutations?
    print(the_string[-1])

has_palindrome_permutation("luci")