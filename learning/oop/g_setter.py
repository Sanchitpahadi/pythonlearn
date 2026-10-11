# Getter Setter in Python


class Circle:
    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError("Radius must be posetive")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2 # I never thought that i can import like this



c = Circle(5)

print(c.area)

c.radius = 10

print(c.area)