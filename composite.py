class Employee:
  def work():
    pass

class ProjectManager(Employee):
  def work(self):
    print('Managmening..,')

class QaEngineer(Employee):
  def work(self):
    print('Testing...')

class SoftwareEngineer(Employee):
  def work(self):
    print('Developing...')

class ProjectComposite:
  employees = [] #components

  def addEmployee(self, employee):
    self.employees.append(employee)

  def removeEmployee(self, employee):
    self.employees.remove(employee)

  def work(self):
    for employee in self.employees:
      employee.work()

pm = ProjectManager()
qa = QaEngineer()
dev = SoftwareEngineer()

project_composite = ProjectComposite()
project_composite.addEmployee(pm)
project_composite.addEmployee(qa)
project_composite.addEmployee(dev)
project_composite.work()

print('to dismiss project manager')
project_composite.removeEmployee(pm)
project_composite.work()

