class Student:
    college = "R.C. Patel Institute of Technology"
    
    
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        
        
    def display_student(self):
        print("Student Name: ",self.name)
        print("Roll Number: ",self.roll_no)
        print("College:",self.college)
        
    
    @classmethod    
    def change_college(cls,new_college):
        cls.college = new_college
  
        
   
        
Student_1 = Student("Winnie",101) 
Student_2 = Student("Rahul",150) 



Students = [Student_1,Student_2]

print("Before changing college:")

for student in Students:
    student.display_student()
    print()


Student.change_college("ABC Institute of Technology")

print("After changing college:")
for student in Students:
    student.display_student()
    print()
   