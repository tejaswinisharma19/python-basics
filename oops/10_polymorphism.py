class Student:
    def introduce(self):
        print("I am a student.")


class Teacher:
    def introduce(self):
        print("I am a teacher.")


student = Student()
teacher = Teacher()

student.introduce()
teacher.introduce()


def introduce_person(person):
    person.introduce()


introduce_person(student)
introduce_person(teacher)