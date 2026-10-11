

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass


class Cat(Animal):

    def speak(self):
        return f"{self.name} says Meeoow"

class Duck(Animal):

    def speak(self):
          return f"{self.name} says Quack"


animals = [Cat("Wishkers") , Duck("Donalds")]

for animal in animals:
    print(animal.speak())