number=int(input('enter the number'))
new=''
for i in str(number):
    if str(number).index(i) % 2 ==1:
        new+=i
print(new)