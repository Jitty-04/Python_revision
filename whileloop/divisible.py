#divisible by 13 and no by 3 between 100 and 500 (100 and 500 excluded)
i=101
while(i < 500):
    if(i % 13 ==0 and i % 3 !=0):
        print(i)
    i+=1