class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, branch):
        super().__init__(name, age)
        self.branch = branch
        
student1 = Student("Winnie", 21, "AIML")

print(student1.name)
print(student1.age)
print(student1.branch)