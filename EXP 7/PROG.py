class Employee:

def __init_(self, name, emp_id, basic_salary):

self.name = name

self.emp_id = emp_id

self.basic_salary = basic_salary

def calculate_gross_salary(self):

#Standard allowances
  hra 0.2* self.basic_salary

da 0.1* self.basic_salary

hra + da

gross_salary = self.basic_salary

return gross_salary

def display_details(self):

print(f"Employee Name: (self.name}")

print("Employee ID: (self.emp_id}")

print(f"Basic Salary: (self.basic_salary}")

print(f"Gross Salary: (self.calculate_gross_salary()}")
