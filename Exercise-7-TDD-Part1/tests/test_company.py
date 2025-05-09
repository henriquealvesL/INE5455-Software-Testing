import pytest

from models.company import Company
from models.employee import Employee
from models.project import Project

def test_1_create_company_w():
  company_w = Company("W's SA")
  assert company_w.name == "W's SA"

def test_2_create_company_without_name():
  with pytest.raises(TypeError):
    Company()

def test_3_create_company_employee(company):
  company.create_employee("João")
  employee_name = company.employees[0].name
  assert employee_name == "João"

def test_4_create_employee_without_name():
  with pytest.raises(Exception):
    Employee()

def test_5_create_employee_without_company():
  with pytest.raises(Exception):
    Employee("João")

def test_6_create_company_project(company):
  company.create_project("Calculator App")
  project_name = company.projects[0].name
  assert project_name == "Calculator App"

def test_7_company_add_employee_to_project(company):
  employee = company.create_employee("João")
  project = company.create_project("Calculator App")
  company.add_employee_to_project(employee, project)
  member_name = project.members[0].name
  assert member_name == "João"

def test_8_company_add_employee_to_non_existent_project(company):
  company_b = Company("B's SA")
  employee = company.create_employee("João")
  project = Project("Delivery app", company_b)

  with pytest.raises(Exception):
    company.add_employee_to_project(employee, project)

def test_9_get_employee_projects(company, employee_joao):
  project = company.create_project("Calculator_app")
  company.add_employee_to_project(employee_joao, project)
  employee_projects = employee_joao.get_projects()
  assert len(employee_projects) == 1

def test_10_create_3_employees(company):    
  company.create_employee("João")
  company.create_employee("Maria")
  company.create_employee("Carlos")
  
  assert len(company.employees) == 3
  assert company.employees[0].name == "João"
  assert company.employees[2].name == "Carlos"

def test_11_create_3_projects(company):
  company.create_project("Calculator App")
  company.create_project("CRM")
  company.create_project("E-Commerce")

  assert len(company.projects) == 3
  assert company.projects[0].name == "Calculator App"
  assert company.projects[2].name == "E-Commerce"

def test_12_add_multiple_projects_to_employee(company_with_projects):
  employee = company_with_projects.create_employee("Matheus")
  employee.add_project(company_with_projects.projects[0])
  employee.add_project(company_with_projects.projects[1])
  
  assert len(employee.projects) == 2

def test_13_add_multiple_members_to_project(company_with_projects, employee_joao):
  employee = company_with_projects.create_employee("Matheus")
  project = company_with_projects.projects[0]
  project.add_member(employee)
  project.add_member(employee_joao)

  assert len(project.members) == 2
