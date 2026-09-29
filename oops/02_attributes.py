class Student():
  def set_data(self,name,age,branch):
   self.name = name
   self.age = age
   self.branch = branch

student1 = Student()
student2 = Student()

student1.set_data("Winnie",21,"AIML")
student2.set_data("Aayush",20,"Computer")

print(student1.name)
print(student1.age)
print(student1.branch)


print(student2.name)
print(student2.age)
print(student2.branch)
