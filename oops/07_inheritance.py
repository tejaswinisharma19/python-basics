class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    
    def __init__(self,name,age,roll_no,course):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.course = course
        

    def display_student(self):
        print("Roll number:",self.roll_no)
        print("Course:",self.course)


student = Student("Winnie", 21, 101, "AIML")

student.display_person()
student.display_student()