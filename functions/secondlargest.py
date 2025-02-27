def second_largest(l):
    largest=l[0]
    second=l[1]
    for i in l:
        if i>largest:
            second=largest
            largest=i
        elif i > second and i <largest:
            second=i
    print(f'second largest={second}')
second_largest([3,8,5,15,10,5,20,5])

# create a function to return the common elements in a given two list

def common(list1, list2):

    # print([i for i in list1 if i in list2])

    print(list(set(list1).intersection(set(list2))))

list1 = [1,2,3,4]

list2 = [3,4,5,6]

common(list1, list2)
