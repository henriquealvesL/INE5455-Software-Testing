import pytest

from models.company import Company

def test_create_company_w1():
  company_w = Company("W's SA")
  assert company_w.name == "W's SA"

def test_create_company_without_name2():
  with pytest.raises(TypeError):
    Company()

