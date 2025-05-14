import pytest

from models.company import Company
from models.employee import Employee

@pytest.fixture
def company():
  return Company("W's SA")

@pytest.fixture
def employee_joao(company):
  return Employee("Joao", company)

@pytest.fixture
def company_with_projects():
  company = Company("B's SA")
  company.create_project("Calculator App")
  company.create_project("CRM")
  return company