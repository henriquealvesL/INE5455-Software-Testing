class Employee:
  def __init__(self, name, company):
    self.name = name
    self.company = company
    self.projects = []

  def get_projects(self):
    return self.projects
  
  def add_project(self, project):
    self.projects.append(project)