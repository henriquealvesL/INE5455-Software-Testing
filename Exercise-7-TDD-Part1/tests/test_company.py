import pytest

from models.company import Company
from models.employee import Employee

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

