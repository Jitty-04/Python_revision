 # WAP to create a function that takes a list of numbers and returns the
# sum of all even numbers

def sum_even(elements):
    sum = 0

    for i in elements:
        if i % 2 == 0:
            sum += i

    print(sum)

sum_even([2,5,7,4,6,3,9,12])
