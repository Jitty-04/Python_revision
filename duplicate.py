text="ABCABC"
new=''
for i in text:
    if i not in new:
        new+=i
print(new)