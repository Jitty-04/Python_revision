items={1:3,2:4,3:6,4:8}
#{3:1,4:2,6:3,8:4}
dict={}
for i in items:
    dict[items[i]] = i
print(dict)