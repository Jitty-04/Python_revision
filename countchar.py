text="hello world"
char=input("enter the character:").strip()
count=0
for i in text:
    if i==char:
        count+=1
if count==0:
    print("not found")
else:
    print(f'count of {char}=',count)






#or


count=0
print(text.count(char) if char in text else "not found")