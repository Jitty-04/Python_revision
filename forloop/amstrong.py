number=int(input('enter number:'))
l=len(str(number))
sum= 0
for digits in str(number):
    sum+= int(digits)**l
print(f'{number} is amstrong' if sum==number else f'{number} is not amstrong')