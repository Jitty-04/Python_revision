# Create a class Marks

# Method 1: Should enter the name of the student, marks of three subjects
# Method 2: Should return name along with average of marks

class Marks:

    def student(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

        print('Data added successfully')

    def average(self):
        print(f'Average mark of {self.name} = {(self.sub1 + self.sub2 + self.sub3) / 3}')

object = Marks()
object.student(name='Hari', sub1=92, sub2=95, sub3=85)

object.average()
