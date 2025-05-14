class Employee:
  def __init__(self, name, company):
    self.name = name
    self.company = company
    self.projects = []
    self.occurrences = []

  def get_projects(self):
    return self.projects
  
  def add_occurrence(self, occurrence):
    if len(self.occurrences) >= 10:
      raise Exception("Employee cannot have more than 10 occurrences")
    
    self.occurrences.append(occurrence)
    
  def get_occurrences(self):
    return self.occurrences
  
  def add_project(self, project):
    self.projects.append(project)