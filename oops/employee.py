# method2 > display details
# method3 > giving a 30% hike in the salary
# method4 > display the updated salary and department and name

class Employee:
    
    def add_user(self, username, salary, dept):
        self.username = username
        self.salary = salary
        self.dept = dept

    def display(self):
        print(f'Name={self.username}')
        print(f'department={self.dept}')
        print(f'salary={self.salary}')

    def hike(self):
        new_salary = self.salary + (self.salary * 30) / 100
        print(f'salary hiked and new salary={new_salary}')
        self.salary = new_salary

    def display_details(self):
        self.display()

obj = Employee()

obj.add_user('Arun', 80000, 'civil')

obj.display()

obj.hike()

obj.display_details()

