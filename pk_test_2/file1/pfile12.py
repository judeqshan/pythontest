
class person:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, weight, height):
      self.weight = weight
      self.height = height

   def displayPerson(self):
      print("height : ", self.height,  ", weight: ", self.weight)