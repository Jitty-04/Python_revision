class student_crm:

    def add_student(self, name, place, age):
        self.name = name
        self.place = place
        self.age = age
        print(f"{name} added successfully")

    def display(self):
        print(self.name, self.place, self.age)


obj1 = student_crm()

# obj1.add_student(name="anna", place="pala", age=21)

# obj1.display()

# obj2 = student_crm()

# obj2.add_student(name="meera", place="pala", age=26)

# obj2.display()

print(type(obj1))

name = "hello"

print(type(name))

"""
<class '__main__.student_crm'>
<class 'str'>
"""
