# Implement a function that checks if a given word is a palindrome

def is_palindrome(word):
    if word.lower()[::-1] == word.lower():
        print('palindrome')
    else:
        print('not palindrome')

is_palindrome('malayalam')
is_palindrome('Malayalam')
is_palindrome('english')
