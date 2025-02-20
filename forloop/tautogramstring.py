#sentence where ll word start with same letter
text="she sells sea shells"
element = text[0]
items = text.split()
for i in items:
    if i[0]!=element:
        print('not a tautogram')
        break
else:
    print('tautogram string')
    
