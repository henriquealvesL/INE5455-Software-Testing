from models.ocurrence import Occurrence

class Project:
  def __init__(self, name, company):
    self.name = name
    self.company = company
    self.members = []
    self.occurrences = []

  def add_member(self, member):
    self.members.append(member)

  def create_occurrence(self, start_date, end_date, description, employee=None):
    if employee:
      if employee not in self.members:
        raise Exception("Employee not a member of the project")
      if len(employee.occurrences) >= 10:
        raise Exception("Employee cannot have more than 10 occurrences")
    
    occurrence = Occurrence(self, start_date, end_date, description, responsible=employee)

    if employee:
      employee.add_occurrence(occurrence)

    self.occurrences.append(occurrence)
    return occurrence