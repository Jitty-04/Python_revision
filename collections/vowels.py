#get vowels from a string and ad it to a list
string=input('enter the strings:')

vowels=[]
for i in string:
    if i in 'aeiouAEIOU':
        vowels.append(i)
print(vowels)