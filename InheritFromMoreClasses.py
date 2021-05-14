
class Animal:
    def __init__(self, animal_name, animal_size):
        self.name = animal_name
        if animal_size in ["small", "medium", "large"]:
            self.size = animal_size
    def __repr__(self):
        return f"animal({self.size})"

class Movements:
    def walk(self, walking_speed=None):
        self.speed = walking_speed
        print(f"walking in {self.speed} m/s")
    def swim(self, swimming_speed=None, swim_depth=None):
        self.speed = swimming_speed
        self.depth = swim_depth
        print(f"swimming in {self.speed} m/s in depth of {self.depth} m")
    def fly(self, height, flying_speed):
        self.altitude = height
        self.velocity = flying_speed
        print(f"flying at {self.altitude} m with {self.velocity} m/s")
    def hop(self, jump):
        self.distance = jump
        print(f" hopping {self.distance} m long")
    
class Wolves(Animal, Movements):
    def __init__(self, animal_name, animal_size, walking_speed):
        if animal_size in ["small", "medium"]:
            super().__init__(animal_name, animal_size)
            super().walk(walking_speed)
    def __repr__(self):
        return f"Wolves({self.size}, {self.name})"

class Bears(Animal, Movements):
    def __init__(self, animal_name, animal_size, walking_speed):
        if animal_size in [ "medium", "large"]:
            super().__init__(animal_name, animal_size)
            super().walk(walking_speed)
    def __repr__(self):
        return f"Bears({self.size}, {self.name})"

class Eagles(Animal, Movements):
    def __init__(self, animal_name, animal_size, fl_height, fl_speed):
        if animal_size in ["small", "medium"]:
            super().__init__(animal_name, animal_size)
            super().fly(fl_height, fl_speed)
    def __repr__(self):
        return f"Eagles({self.size}, {self.name})"

class Ducks(Animal, Movements):
    def __init__(self, animal_name, animal_size, sw_depth, sw_speed):
        if animal_size in ["small", "medium"]:
            super().__init__(animal_name, animal_size)
            super().swim(sw_speed, sw_depth)
    def __repr__(self):
        return f"Ducks({self.size}, {self.name})"

class Frogs(Animal, Movements):
    def __init__(self, animal_name, sw_depth, sw_speed, jump_length):
        super().__init__(animal_name, animal_size="small")
        super().swim(sw_speed, sw_depth)
        super().hop(jump_length)
    def __repr__(self):
        return f"Frogs({self.name}, {self.depth}, {self.size})"

class Trout(Animal, Movements):
    def __init__(self, animal_name, sw_depth, sw_speed):
        super().__init__(animal_name, animal_size="small")
        super().swim(sw_speed, sw_depth)
    def __repr__(self):
        return f"Trout({self.name}, {self.depth}, {self.size})"

wolf01 = Wolves("scoopy-doo", "small", 3)
wolf02 = Wolves("greywolf", "medium", 5)
print(wolf01)
wolf01.walk()
print(wolf02)
bear01 = Bears("arthur", "medium", 4)
print(bear01)
frog01 = Frogs("king", 2, 5, 1)
print(frog01)
# I do not want the frog to be able to walk,
# and this is the problem with my desing (having 1 big Movement class with many methods)
frog01.walk(5)  

