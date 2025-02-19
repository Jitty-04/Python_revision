#input: s = "A man, a plan, a canal: Panama"
#OUTPUT:TRUE
#explaination:"amanaplanacanalpanama"

string="A man, a plan, a canal: Panama"
str=""
for i in string.lower():
    if i.isalpha():
        str += i
if str[::-1] == str:
    print('string is palindrome')
else:
    print("not palindrome")