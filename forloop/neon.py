#sum of digits of square of number = number
#9-> 9^2 = 81 8 +1 = 9

number= int(input('enter the number'))
square=number**2
sum=0
for digits in str(square):
    sum += int(digits)
print(f'{number} is neon' if sum==number else f'{number} is not neon')