#sum of proper divisors(excluding itself) = number
#28 -> 1+2+4+7+14 =28
number=int(input('enter the number'))
sum=0
for i in range(1,number//2+1):
    if number%i==0:
        sum+=i
print(f'{number} is perfect' if sum==number else f'{number} is not perfect')