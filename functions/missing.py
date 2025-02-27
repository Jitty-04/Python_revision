# create a function to identify the missing number from the sequence of numbers from a list

# items = [3,7,6,4]

def missing(items):

    for i in range(min(items), max(items)):

        if i not in items:
            print(i)

missing([3,7,6,4])
