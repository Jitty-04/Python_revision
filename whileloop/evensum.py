# 1 to n
i=1
n=int(input("enter the last number"))
sum=0
while(i<=n):
    if i % 2 ==0:
        sum+=i
    i+=1
print(sum)