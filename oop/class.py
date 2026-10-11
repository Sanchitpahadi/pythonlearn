


class Dog:

    def __init__(self , name , breed):
        self.name = name
        self.breed = breed


    def bark(self):
        print(f"{self.name} says : Woffff !")

    def __str__(self):
        return f"{self.name}({self.breed}) "


dog1 = Dog("Rex","German Shephered")

dog2 = Dog("buddy","golden retriver")


dog1.bark()

print(dog2)
