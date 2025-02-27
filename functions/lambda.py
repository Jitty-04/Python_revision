"""
anonymous function - fun. without name

they are useful for short functions and don't need full 'def' block

can give any number of arguments

only one expression
"""

# lambda arguments : expression

# result = lambda a, b : a + b

# print(result(3, 4))

# 1. return avg of 3 numbers

# result = lambda a, b, c : (a + b + c) / 3

# print(result(5, 10, 15))

# 2. check if a number is even or odd

# result = lambda a : 'even' if a % 2 == 0 else 'odd'

# print(result(10))

# print(result(5))

# 4. maximum of 3 numbers

# result = lambda a, b, c : max(a, b, c)
# result = lambda a, b, c : max(a, b, c)

# print(result(10, 5, 25))

# 5. reverse a string

# result = lambda s : s[::-1]

# print(result('dhruv'))

# 6. check if a string is palindrome

# result = lambda s : 'palindrome' if s == s[::-1] else 'not palindrome'

# print(result('malayalam'))

# 7. check if a number is +ve, -ve or 0

# result = lambda n : 'positive' if n > 0 else 'negative' if n < 0 else 'zero'

# print(result(2))
# print(result(-1))
# print(result(0))

# check whether the letter is consonant or vowel

result = lambda a : 'vowel' if a in 'aeiou' else 'consonant'

print(result('a'))
print(result('b'))


