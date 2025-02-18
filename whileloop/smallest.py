#smallest digit of a number
number=int(input("enter the number"))
# smallest=9
# while(number>0):
#     digit=number%10
#     if digit<smallest:
#         smallest=digit
#     number //=10
# print(smallest)
smallest=str(number)[0]
for i in str(number):
    if i < smallest:
        smallest=i
print(smallest)