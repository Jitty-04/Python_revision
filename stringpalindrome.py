string=input('enter the string').strip()
rev=''
for i in string:
    rev=i+rev
if rev==string:
    print(f'{string} is palindrome')
else :
    print(f'{string} is not palindrome')

