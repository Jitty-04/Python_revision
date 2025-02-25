#word as key length as value
text="python is a programming language"
new={}
l=0
longest=""
for i in text.split():
    new[i] = len(i)
    if len(i) > l:
        l=len(i)
        longest=i
print(longest)
print(new)