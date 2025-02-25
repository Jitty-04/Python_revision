list=[1,2,1,1,2,3,4,5,5]
#op[1:3,2:2,3:1...]
dict={}
for i in list:
    dict[i] = list.count(i)
print(dict)