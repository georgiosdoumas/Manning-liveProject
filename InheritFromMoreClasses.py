# The following does not work, it seems that the way I tried to use
# super(name-of-base-class).method-of-base-class
# is not accepted syntax. So I did not want to spent time to try things out
# and abandonded it

class Animal:
    def __init__(self, animal_name, animal_size):
        self.name = animal_name
        if animal_size in ["small", "medium", "large"]:
            self.size = animal_size
    def __repr__(self):
        return f"animal({self.size})"

class Movements:
    def walk(walking_speed):
        print(f"walking in {speed} m/s")
        self.speed = walking_speed
    def swim(swimming_speed, swim_depth):
        self.speed = swimming_speed
        self.depth = swim_depth
        print(f"swimming in {speed} m/s in depth of {depth} m")
    def fly(height, flying_speed):
        self.altitude = height
        self.velocity = flying_speed
        print(f"flying at {altitude} m with {velocity} m/s")
    def hop(jump):
        self.distance = jump
        print(f" hopping {distance} m long")
    
class Wolves(Animal, Movements):
    def __init__(self, animal_name, animal_size, walking_speed):
        if animal_size in ["small", "medium"]:
            super(Animal).__init__(animal_name, animal_size)
            super(Movements).walk(walking_speed)
    def __repr__(self):
        return f"Wolves({self.size}, {self.name})"

class Bears(Animal, Movements):
    def __init__(self, animal_name, animal_size, walking_speed):
        if animal_size in [ "medium", "large"]:
            super(Animal).__init__(animal_name, animal_size)
            super(Movements).walk(walking_speed)
    def __repr__(self):
        return f"Bears({self.size}, {self.name})"

class Eagles(Animal, Movements):
    def __init__(self, animal_name, animal_size, fl_height, fl_speed):
        if animal_size in ["small", "medium"]:
            super(Animal).__init__(animal_name, animal_size)
            super(Movements).fly(fl_height, fl_speed)
    def __repr__(self):
        return f"Eagles({self.size}, {self.name})"

class Ducks(Animal, Movements):
    def __init__(self, animal_name, animal_size, sw_depth, sw_speed):
        if animal_size in ["small", "medium"]:
            super(Animal).__init__(animal_name, animal_size)
            super(Movements).swim(sw_speed, sw_depth)
    def __repr__(self):
        return f"Ducks({self.size}, {self.name})"

class Frogs(Animal, Movements):
    def __init__(self, animal_name, sw_depth, sw_speed, jump_length):
        super().__init__(animal_name, animal_size="small")
        super(Movements).swim(sw_speed, sw_depth)
        super(Movements).hop(jump_length)
    def __repr__(self):
        return f"Frogs({self.name}, {self.depth}, {self.size})"

class Trout(Animal, Movements):
    def __init__(self, animal_name, sw_depth, sw_speed):
        super().__init__(animal_name, animal_size="small")
        super(Movements).swim(sw_speed, sw_depth)
    def __repr__(self):
        return f"Trout({self.name}, {self.depth}, {self.size})"

wolf01 = Wolves("scoopy-doo", "small", 3)
wolf02 = Wolves("greywolf", "medium", 5)
print(wolf01)
print(wolf02)
bear01 = Bears("arthur", "medium", 4)
print(bear01)
frog01 = Frogs("king", 2, 5, 1)
print(frog01)
frog01.swim()

