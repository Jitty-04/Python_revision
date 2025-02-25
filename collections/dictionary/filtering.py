data={"a":5,"b":2,"c":10,"d":3,"e":8}
#value greater than 5
for i in data.copy(): #shallow copy of data.length not changed even pop is done
    if data[i] <= 5:
        data.pop(i)
print(data)