class Animal:
    def __init__(self, animal_size="small"):
        if animal_size in ["small", "medium", "large"]:
            self.size = animal_size
    def __repr__(self):
        return f"animal({self.size})"

class Wolves(Animal):
    def __init__(self, animal_size, animal_name):
        if animal_size in ["small", "medium"]:
            super().__init__(animal_size)
        self.name = animal_name
    def __repr__(self):
        return f"Wolves({self.size}, {self.name})"

class Bears(Animal):
    def __init__(self, animal_size, animal_name):
        if animal_size in [ "medium", "large"]:
            super().__init__(animal_size)
        self.name = animal_name
    def __repr__(self):
        return f"Bears({self.size}, {self.name})"

class Eagles(Animal):
    def __init__(self, animal_size, animal_name):
        if animal_size in ["small", "medium"]:
            super().__init__(animal_size)
        self.name = animal_name
    def __repr__(self):
        return f"Eagles({self.size}, {self.name})"

class Ducks(Animal):
    def __init__(self, animal_size, animal_name):
        if animal_size in ["small", "medium"]:
            super().__init__(animal_size)
        self.name = animal_name
    def __repr__(self):
        return f"Ducks({self.size}, {self.name})"

class Frogs(Animal):
    def __init__(self, animal_name, swimming_depth, animal_size="small"):
        super().__init__(animal_size)
        self.name = animal_name
        self.depth = swimming_depth
    def swim(self):
        print(f"{self.name} swimming at depth {self.depth} feet")
    def __repr__(self):
        return f"Frogs({self.name}, {self.depth}, {self.size})"

class Trout(Animal):
    def __init__(self, animal_name, swimming_depth, animal_size="small"):
        super().__init__(animal_size)
        self.name = animal_name
        self.depth = swimming_depth
    def swim(self):
        print(f"{self.name} swimming at depth {self.depth} feet")
    def __repr__(self):
        return f"Trout({self.name}, {self.depth}, {self.size})"

wolf01 = Wolves("small", "scoopy-doo")
wolf02 = Wolves("medium", "greywolf")
print(wolf01)
print(wolf02)
bear01 = Bears("medium", "arthur")
print(bear01)
frog01 = Frogs("king", 2)
print(frog01)
frog01.swim()

