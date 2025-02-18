text="hellopython" #ollehpython
for i in text:
    if i=="p":
        element=text.index("p")
        print(text[:element][::-1]+text[element:])