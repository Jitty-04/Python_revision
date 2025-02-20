# number divisible by sum of its digits
number=int(input('enter the number'))
sum=0
for i in str(number):
    sum += int(i)
print(f'{number} is harshad' if number % sum==0 else f'{number} is not harshad')