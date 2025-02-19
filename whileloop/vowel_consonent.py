text='programminglanguag'
v=0
c=0
for i in text:
    if i in 'aeiouAEIOIU':
        v+=1
    else:
        c+=1
print('vowel count:',v)
print('consonant:',c)
