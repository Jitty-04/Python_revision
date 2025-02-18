#sum of numbers entered by user until user enter 0
number=int(input("enter the number"))
sum=0
while(number != 0):
    sum+=number
    number=int(input("enter the number"))
print(sum)