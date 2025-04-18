# Defining a Superhero class
class Superhero:
    def __init__(self, name, alias, power, weakness):
        self.name = name
        self.alias = alias
        self.power = power
        self.weakness = weakness

    def introduce(self):
        return f"I'm {self.name}, known as {self.alias}. My superpower is {self.power}, but my weakness is {self.weakness}."

# Subclass to demonstrate inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, power, weakness, flight_speed):
        super().__init__(name, alias, power, weakness)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.alias} is flying at {self.flight_speed} km/h!"

# Creating objects
superhero_1 = Superhero("Bruce Wayne", "Batman", "Intelligence", "Trust issues")
superhero_2 = FlyingSuperhero("Clark Kent", "Superman", "Strength", "Kryptonite", 800)

print(superhero_1.introduce())
print(superhero_2.introduce())
print(superhero_2.fly())
