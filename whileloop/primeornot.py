number=int(input('enter the number'))
if number > 1:
    for i in range(2,number):
        if number % i ==0:
            print('not a prime')
            break
    else:
        print('prime')
else:
    print('enter a valid number')