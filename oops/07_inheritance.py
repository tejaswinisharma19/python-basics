class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")


student1 = Student("Alice", 20)

student1.introduce()
student1.study()