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