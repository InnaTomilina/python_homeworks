class Person:
    def __init__(self, first_name, last_name):
        self.age = None
        self.first_name = first_name
        self.last_name = last_name

    def set_age(self, age):
        self.age = age


class Teacher(Person):
    def __init__(self, first_name, last_name, specialty):
        super().__init__(first_name, last_name)
        self.specialty = specialty
        self.working_hours = None
        self.salary = None

    def set_salary(self, salary):
        self.salary = salary

    def set_working_hours(self, working_hours):
        self.working_hours = working_hours

    def __str__(self):
        return f'Teacher salary is {self.salary} and working hours per day are {self.working_hours}'

class Student(Person):
    def __init__(self, first_name, last_name, classroom):
        super().__init__(first_name, last_name)
        self.classroom = classroom
        self.parents = []

    def add_parent(self, first_name, last_name, phone_number):
        parent = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
        }

        self.parents.append(parent)

t = Teacher ("Inna", "Tomilina", "teacher")
t.set_salary(30000)
t.set_working_hours(8)
print(t)

s = Student ("Ivan", "Ivanov", "9A")
print(s.first_name)
s.add_parent("Anton", "Antonov", "12345")
print(s.parents)

