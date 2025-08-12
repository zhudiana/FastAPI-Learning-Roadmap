class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"This is {self.name} and I am {self.age} years old.")

# Child class
class Student(Person):
    pass

x = Student("John", 34)
x.print_info()