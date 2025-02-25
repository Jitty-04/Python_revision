text="apple123 banana45 cherry78"
#if digit sum
dict={}
for i in text.split():
    sum=0
    for j in i:
        if j.isdigit():
            sum += int(j)
    dict[i] = sum
print(dict)