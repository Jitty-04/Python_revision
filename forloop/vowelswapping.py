text='icecream'
list=[]
new=''
for i in text:
    if i in 'aeiouAEIOU':
        list.append(i)
list1=list[::-1]
for i in text:
    if i in 'aeiouAEIOU':
        new += list1[0]
        list1.pop(0)
    else:
         new += i
print(new)