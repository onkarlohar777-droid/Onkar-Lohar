class Employee:

def _init_(self, name, basic_salary):
self.name = name
self.basic_salary = basic_salary
def calculate_salary(self, bonus):
if bonus < 0:
print("Invalid bonus amount")

else:
total_salary = self.basic_salary + bonus
print(f"Employee Name: (self.name}")
print(f"Basic Salary: {self.basic_salary)")
print(f"Bonus: (bonus)")
print(f"Total Salary: {total_salary)")

