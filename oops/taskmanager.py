# Class Taskmanager

# method1 > name, taskname, completed

# method2 > update task

# method3 > delete task

class Todo:

    def add_task(self, name, taskname, completed=False):
        self.name = name
        self.task = {}

        self.task[name] = {"tname": taskname, "status": completed}

        #  {'Arun': {'tname': 'python', 'status': False}}

        print("task added successfully")

    def update_task(self):
        self.task[self.name]["status"] = True
        print(self.task)

    def display(self):
        print(self.task)

    def delete_task(self, name):
        if name in self.task:
            self.task.pop(name)
            print("task deleted")
        else:
            print("not found")

    def __str__(self):
        # to represent an object as a string when it is printed
        return self.name


obj1 = Todo()
obj1.add_task("Arun", "python")

print(obj1)

obj2 = Todo()
obj2.add_task("Amal", "Java")

obj1.display()
obj1.update_task()
obj1.delete_task("Amal")
