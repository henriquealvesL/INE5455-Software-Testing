class Project:
  def __init__(self, name, company):
    self.name = name
    self.company = company
    self.members = []

  def add_member(self, member):
    self.members.append(member)