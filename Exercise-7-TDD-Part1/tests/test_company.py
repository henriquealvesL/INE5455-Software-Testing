from models.company import Company

def test_create_company_w():
  company_w = Company("W's SA")
  assert company_w.name == "W's SA"
