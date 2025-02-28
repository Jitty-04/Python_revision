from functools import reduce

# functools.py >> def reduce()
# reduce

# sum of numbers
numbers = [1,2,3,4]

print(reduce(lambda a, b: a + b, numbers))  # a = 1, b = 2  a + b >> 3    |    a = 3, b = 3   3 + 3   |    a = 6, b = 4
print(reduce(lambda a, b: a * b, numbers))

numbers = [4,3,5,6,2,6,7,8,9]

"""
double each number in the given list
filter out the numbers that are not divisible by 3 from the doubled numbers
find the sum of the remaining numbers
"""

numbers = [4,3,5,6,2,6,7,8,9]

result = list(map(lambda a: a**2, numbers))

print(result)

new = list(filter(lambda a: a % 3 != 0, result))

print(new)

print(reduce(lambda a, b: a + b, new))
