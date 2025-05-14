from enum import Enum

class Occurrence:
  _id_counter = 1 

  def __init__(self, project, start_date: str, end_date: str, description: str, responsible=None, type=None, priority=None):
    self.id = Occurrence._id_counter
    self.project = project
    Occurrence._id_counter += 1
    self.start_date = start_date
    self.end_date = end_date
    self.description = description
    self.responsible = responsible
    self.status = Status.OPEN
    self.type = type
    self.priority = priority


  def add_responsible(self, employee):
    if employee not in self.project.members:
      raise Exception("Employee not a member of the project")
    
    if len(employee.occurrences) >= 10:
      raise Exception("Employee cannot have more than 10 occurrences")
    
    employee.add_occurrence(self)
    self.responsible = employee

class Status(Enum):
  OPEN = "OPEN"
  FINISH = "FINISH"
  WORKING = "WORKING"

class Type(Enum):
  TASK = 1
  BUG = 2
  IMPROVEMENT = 3
  
class Priority(Enum):
  LOW = 1
  MEDIUM = 2  
  HIGH = 3  

