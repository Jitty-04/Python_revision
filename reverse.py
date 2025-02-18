number=int(input('enter the number:'))
rev=''
for i in str(number):
    rev=i+rev
print(rev)

#or

number=12345
print(str(number)[::-1])