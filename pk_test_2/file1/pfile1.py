from file1.pfile12 import person
# from pfile12 import person


class EmployeePfile1(person):
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary, weight, height):
      super(EmployeePfile1,self).__init__(weight, height)
      self.name = name
      self.salary = salary
      EmployeePfile1.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % EmployeePfile1.empCount)
 
   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)