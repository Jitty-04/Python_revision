# check the prime numbers from a range of numbers from a to b

a = int(input('enter the start: '))
b = int(input('enter the stop: '))

for i in range(a, b+1):

    if i <= 1:
        print('not valid')
    
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
