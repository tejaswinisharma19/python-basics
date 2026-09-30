class Student:
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display_details(self):
        print("Student Name:", self.name)
        print("Student Roll No.:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())

    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            return "A+"
        elif 80 <= self.marks <= 89:
            return "A"
        elif 70 <= self.marks <= 79:
            return "B"
        elif 60 <= self.marks <= 69:
            return "C"
        elif 50 <= self.marks <= 59:
            return "D"
        else:
            return "F"

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.marks = new_marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks.")


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully.")

    def display_all_students(self):
        print("\n--- All Students ---")

        for student in self.students:
            student.display_details()
            print()

    def find_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent Found:")
                student.display_details()
                return

        print("Student not found.")

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found.")



student1 = Student("Winnie", 101, "AIML", 85)
student2 = Student("Alice", 102, "CSE", 92)
student3 = Student("Rahul", 103, "ECE", 74)

management = StudentManagement()

management.add_student(student1)
management.add_student(student2)
management.add_student(student3)


management.display_all_students()


management.find_student(102)


student1.update_marks(95)


management.display_all_students()


management.remove_student(103)


management.display_all_students()

management.find_student(999)