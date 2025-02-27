# wap to find the most frequent element in a list using function

def frequent(list):
    max = 0
    element = ''

    for i in list:
        if list.count(i) > max:
            max = list.count(i)
            element = i

    print(f"most frequent element ={element} and count={max}")

frequent([1,2,1,3,1,4,2,3])
