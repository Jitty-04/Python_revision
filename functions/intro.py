"""
print()
len()
input()
range()
sum()
"""

print("hello gud evng")

def greet():  # function header
    print("hello gud evng")  # function body

greet()  # function caller

def addition(a, b):
    print(a + b)

addition(8, 7)
addition(10, 15)
addition(-8, 7)

def add(a, b):
    return a + b  # return statement used to return the value towards the function caller

print(add(2, 3))


def details(name, place, course, company="Luminar"):  # parameters, company is a default argument
    # it takes a default value if the user doesn't give an argument.
    print(f"Hi {name}, you are from {place} and doing the course {course} at {company}")

details('jitty', 'pta', 'python')  # arguments

details('pta', 'jitty', 'python')  # order changed

details(place='chennai', course='python', name='jitty')  # keyword arguments - don't bother about the order of arguments


def add(*args):  # n number of arguments, args is a tuple object -> tuple
    print(args)

    sum = 0
    for i in args:
        sum += i

    print(sum)

add(1, 2)
add(1, 2, 3)

# -------------------------------------
# DECORATOR
# -------------------------------------

"""
a design pattern in python that allows a user to add new functionality to an existing
object without modifying its structure
"""

# def swap_members(fn):  # def swap_members(division(2,0))

#     def wrapper(a,b):  # def wrapper(a=2,b=0)

#         if b == 0:      # b = 0

#             a,b = b,a   # a,b= 0,2

#         return fn(a,b)  # return division(a=0,b=2)

#     return wrapper


# @swap_members
# def division(a,b):  # division(2,0)

#     print(a/b)

# # division(2,0)

def check_pwd(fn):

    def wrapper(a):

        if a == "admin":
            return fn()
        else:
            print("Access Denied")

    return wrapper

@check_pwd
def db():
    print("db deleted")
db('user')
db('admin')


