class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"I study {self.branch}")

student1 = Student("Winnie", 21, "AIML")
student2 = Student("Aayush", 20, "Computer")

student1.introduce()
student2.introduce()