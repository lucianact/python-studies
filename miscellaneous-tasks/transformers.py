# filter()

# find odds:
def are_numbers_odd(x):
    if x % 2 == 0:
        return False
    return True

nums = (1, 2, 3, 4, 5, 5, 6, 7, 8)
odds = list(filter(are_numbers_odd, nums))
print(odds)

# find lower case:
def are_lowercase(y):
    if y.isupper():
        return False
    return True 

chars = "AURHfoenvb"
lower = list(filter(are_lowercase, chars))
print(lower)

# map
def square(z):
    return z * z 

squares = list(map(square, nums))
print(squares)

def letter_grade(w):
    if w >= 90:
        return "A"
    elif w < 90 and w >= 80:
        return "B"
    return "C"

grades = (90, 60, 70, 80)
grades_converted = list(map(letter_grade, grades))
print(grades_converted)


# # Write a function that returns the sum of integers in an
# # arbitrarily nested list of lists, where each integer is
# # weighted multiplicatively by the "depth" of its level.
# # For example, the following inputs should return the following outputs:
# input_A = [1, 2, 3]
# #weighted_sum(input_A) == 6
# input_B = [1, [2, 3]]
# #weighted_sum(input_B) == 1 * 1 + (2 + 3) * 2 ==  11
# input_C = [1, [2, [3, 4]]]
# #weighted_sum(input_C) == 1 * 1 + 2 * 2 + (3 + 4) * 3 == 26

# function greet (person) {
#   if (person == { name: 'amy' }) {
#     return 'hey amy'
#   } else {
#     return 'hey arnold'
#   }
# }

# console.log(greet({ name: 'amy' }))

# let amy = { name: 'amy' }

# function greet (person) {
#   if (person.name == 'amy') {
#     return 'hey amy'
#   } else {
#     return 'hey arnold'
#   }
# }
# console.log(greet(amy))