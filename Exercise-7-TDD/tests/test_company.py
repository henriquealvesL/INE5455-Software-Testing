import pytest

from models.company import Company
from models.employee import Employee
from models.project import Project
from models.ocurrence import Status, Type, Priority

def create_10_occurrences(company, project, employee):
  occurrences = []
  for i in range(10):
    occurrence = project.create_occurrence(f"2023-10-{i+1}", f"2023-10-{i+2}", f"Occurrence {i+1}", employee)
    occurrences.append(occurrence)
  return occurrences

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

def test_14_company_create_ocurrence(company_with_projects):
  project = company_with_projects.projects[0]
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting")
   
  assert occurrence.start_date == "2023-10-01"
  assert occurrence.end_date == "2023-10-02"
  assert occurrence.description == "Meeting"

def test_15_add_employee_to_ocurrence(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting")
  occurrence.add_responsible(employee)

  assert employee in project.members
  assert occurrence.responsible == employee

def test_16_add_employee_to_ocurrence_not_member_of_project(company_with_projects):
  project = company_with_projects.projects[0]
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting")
  employee = company_with_projects.create_employee("Matheus")

  with pytest.raises(Exception):
    occurrence.add_responsible(employee)

def test_17_get_employee_ocurrences(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting")
  occurrence_2 = project.create_occurrence("2023-10-03", "2023-10-04", "Workshop")
  occurrence.add_responsible(employee)
  occurrence_2.add_responsible(employee)
  
  employee_ocurrences = employee.get_occurrences()
  
  assert len(employee_ocurrences) == 2
  assert employee_ocurrences[0].description == "Meeting"
  assert employee_ocurrences[1].description == "Workshop"

def test_18_add_eleventh_occurrence_to_employee(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  create_10_occurrences(company_with_projects, project, employee)
  
  occurrence_11 = project.create_occurrence("2023-10-11", "2023-10-12", "Occurrence 11")
  
  with pytest.raises(Exception):
    employee.add_occurrence(occurrence_11)

def test_19_verify_occcurrence_status_open(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting")
  occurrence.add_responsible(employee)
  
  assert occurrence.status == Status.OPEN

def test_20_verify_occcurrence_status_finish(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting")
  occurrence.add_responsible(employee)
  
  occurrence.status = Status.FINISH
  
  assert occurrence.status == Status.FINISH

def test_21_verify_occcurrence_status_working(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting")
  occurrence.add_responsible(employee)
  
  occurrence.status = Status.WORKING
  
  assert occurrence.status == Status.WORKING

def test_22_verify_occurrence_type(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting", type=Type.TASK)

  assert occurrence.type == Type.TASK

def test_23_verify_occurrence_priority(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting", priority=Priority.HIGH)

  assert occurrence.priority == Priority.HIGH

def test_24_add_invalid_member_to_occurrence(company_with_projects, employee_joao):
  project = company_with_projects.projects[0]

  with pytest.raises(Exception):
    project.create_occurrence("2023-10-01", "2023-10-02", "Meeting", employee_joao)

def test_25_project_create_eleventh_employee_occurrence(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  create_10_occurrences(company_with_projects, project, employee)
    
  with pytest.raises(Exception):
    project.create_occurrence("2023-10-11", "2023-10-12", "Occurrence 11", employee)

def test_26_occurrence_add_responsible_with_ten_occurrences(company_with_projects):
  project = company_with_projects.projects[0]
  employee = company_with_projects.create_employee("Matheus")
  project.add_member(employee)
  create_10_occurrences(company_with_projects, project, employee)
  
  occurrence = project.create_occurrence("2023-10-11", "2023-10-12", "Occurrence 11")
  
  with pytest.raises(Exception):
    occurrence.add_responsible(employee)

def test_27_change_occurrence_responsible(company_with_projects):
  project = company_with_projects.projects[0]
  employee_1 = company_with_projects.create_employee("Matheus")
  employee_2 = company_with_projects.create_employee("João")
  project.add_member(employee_1)
  project.add_member(employee_2)
  
  occurrence = project.create_occurrence("2023-10-01", "2023-10-02", "Meeting", employee_1)
  
  occurrence.add_responsible(employee_2)
  
  assert occurrence.responsible == employee_2
