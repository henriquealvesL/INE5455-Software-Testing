from models.employee import Employee

class Company():
  def __init__(self, name):
    self.name = name
    self.employees = []

  def create_employee(self, name):
    employee = Employee(name)
    self.employees.append(employee)