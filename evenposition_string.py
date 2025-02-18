string=input('enter the string').strip()
l=len(string)
for i in range(l):
    if i % 2==0:
        print(string[i],end="")
    
