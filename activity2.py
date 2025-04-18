# Creating classes with the same action
class Animal:
    def move(self):
        pass

class Car(Animal):
    def move(self):
        return "Driving"

class Plane(Animal):
    def move(self):
        return "Flying"

class Fish(Animal):
    def move(self):
        return "Swimming"

# Testing polymorphism
objects = [Car(), Plane(), Fish()]

for obj in objects:
    print(obj.move())
