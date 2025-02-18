#wap to print the factors of a number entered by user
i=1
number=int(input("enter the number:"))
while(i <= number/2):
    if number % i == 0:
        print(i)
    i += 1
