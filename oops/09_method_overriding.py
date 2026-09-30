class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
        
        
    def work(self):
        print("Name:",self.name)
        print("Employee ID:",self.employee_id)
        
        
class Developer(Employee):
    
    def work(self):
        print(f"{self.name} is developing software.")
         
class Designer(Employee):
    
    def work(self):
        print(f"{self.name} is designing the user interface.")
        
developer = Developer("Alice", 101)
designer = Designer("Bob",190)

developer.work()
designer.work()
    