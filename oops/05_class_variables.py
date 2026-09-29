class Student:
    college = "RCPIT"

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch


student1 = Student("Winnie", 21, "AIML")
student2 = Student("Aayush", 20, "Computer")

print(student1.name)
print(student1.college)

print(student2.name)
print(student2.college)