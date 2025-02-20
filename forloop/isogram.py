#string in which no letter repeats

text=input('enter the string:')
for i in text:
    if text.count(i)>1:
        print('not isogram')
        break
else:
    print('isogram')