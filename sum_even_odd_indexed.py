number=int(input('enter the number'))
even_sum=0
odd_sum=0
index=0
for i in str(number):
    if index % 2 ==0:
        even_sum+=int(i)
    else:
        odd_sum+=int(i)
    index+=1
print(f'sum of even indexed numbers={even_sum} & sum of odd indexed numbers={odd_sum}')
    