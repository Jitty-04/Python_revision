# create a function to find the first recursive element in a string

# def first_recursive(string):
#     for i in string.lower():
#         if string.count(i) > 1:
#             print(i)
#             break

# first_recursive('hellooo')

# create a function to find first consecutively most repeating character

# input = "programming"
# output = m

def consecutive(string):

    for i in range(len(string)):
        if string[i] == string[i+1]:
            print(string[i])
            break

consecutive("programming")
consecutive("hellooomm")
