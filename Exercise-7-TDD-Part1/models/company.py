from models.employee import Employee
from models.project import Project

class Company():
  def __init__(self, name):
    self.name = name
    self.employees = []
    self.projects = []

  def create_employee(self, name):
    employee = Employee(name, company=self)
    self.employees.append(employee)

    return employee

  def create_project(self, name):
    project = Project(name, company=self)
    self.projects.append(project)

    return project

  def add_employee_to_project(self, employee, project):
    if project not in self.projects:
      raise ValueError("The project does not exist in the company.")
    
    employee.add_project(project)
    project.add_member(employee)