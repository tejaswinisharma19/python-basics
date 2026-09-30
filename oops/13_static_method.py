class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_student(self):
        print("Student Name:",self.name)
        print("Age:",self.age)
        
    @staticmethod
    def is_eligible(age):
        if age >= 18:
            return True
        else:
            return False
        
student_1 = Student("Winnie",21)
student_2 = Student("Aayush",20)
student_3 = Student("Siya",15)

Students = [student_1,student_2,student_3]

for student in Students:
    student.display_student()
    
    student_eligible = Student.is_eligible(student.age)
    print("Is Eligible:",student_eligible)
    