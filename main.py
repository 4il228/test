class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        print('Student:')
        print(self.name)
        print(self.surname)
        print(self.age)