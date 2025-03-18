class Otter:
    def __init__(self, species, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.species = species
        self.weight = "3 kg"
class Duck:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.beak = "Has beak"
class Platypus (Otter, Duck):
    def print_info(self):
        print(self.species)
        print(self.weight)
        print(self.beak)
animal = Platypus(species ="Platypus")
animal.print_info()