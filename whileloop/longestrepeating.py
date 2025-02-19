text="programminglanguage"
most_recursive=0
char=''
for i in text:
    if text.count(i) > most_recursive:
        most_recursive=text.count(i)
        char=i
print(char)