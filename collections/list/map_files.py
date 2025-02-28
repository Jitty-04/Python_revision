# create a function to accept a number and return its squared value

# The map() function executes a given function to each element of an iterable (such as lists, tuples)

# numbers = [1,2,3,4,5]
# print(list(map(lambda a: a**2, numbers)))

# list of words are given return list of their length

# words = ["hello","welcome","python"]    # [5,7,6]
# print(list(map(lambda words: len(words), words)))

# words = ["hello","welcome","python"]    # o/p >> ["Hello","Welcome","Python"]
# print(list(map(lambda words: words.capitalize(), words)))

# words = ["abc","def","ghi"]   # o/p >> ["cba","fed","ihg"]
# print(list(map(lambda words: words[::-1], words)))

# elements = ["1","2","3"]   # o/p >> [1,2,3]
# print(list(map(lambda elements: int(elements), elements)))

# selects elements from an iterable based on the result of a function
# ============================================

# numbers = [1,2,3,4,5]
# print(list(filter(lambda a: a%2==0, numbers)))

# elements = ["hi","hello","hut","python"]
# get the words with more than 3 letters

# print(list(filter(lambda a: len(a) > 3 ,elements)))

# write a program that accepts a string and filter vowels from it.

text = "hello world"    # o/p >> "eoo"

print(list(filter(lambda a: a in "aeiou", text)))