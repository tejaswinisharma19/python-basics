class Employee:
    def __init__(self,name,employee_id,basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary
        
    def display_employee(self):
        print("Name:",self.name)
        print("Employee ID:",self.employee_id)
        print("Basic Salary:",self.basic_salary)
        print("Final Salary:",self.calculate_salary())
        
    def calculate_salary(self):
        print("Calculating salary for",self.name)
        
class Developer(Employee):
    
    def __init__(self, name, employee_id, basic_salary):
        super().__init__(name, employee_id, basic_salary)

    def calculate_salary(self):
        final_salary = self.basic_salary + (self.basic_salary * 0.2)
        return final_salary

class Manager(Employee):
    def __init__(self, name, employee_id, basic_salary):
        super().__init__(name, employee_id, basic_salary)

    def calculate_salary(self):
        final_salary = self.basic_salary + (self.basic_salary * 0.3)
        return final_salary

developer = Developer("Alice", 101, 50000)
manager = Manager("Bob", 102, 70000)

employees = [developer, manager]

for employee in employees:
    employee.display_employee()