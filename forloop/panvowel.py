#all vowel exactly once

text=input('enter the string').strip()
vowel='aeiou'
for i in vowel:
    if i not in text.lower():
        print('not panvowel')
        break
else:
    print('panvowel')
    