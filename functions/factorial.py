# create a function to find the factorial of a given number

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print(fact)

factorial(4)
