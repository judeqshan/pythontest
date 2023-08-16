class Animal():
    def __init__(self, name) -> None:
        pass
    
    def eat(self):
        print("aninaml eat....")
        

class Dog(Animal):
    def __init__(self,name) -> None:
        super().__init__(name)
        

dog = Dog("huahua")
dog.eat()