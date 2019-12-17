from .characters import Person
class Guerrier(Person):
    """class for guerrier player"""
    def __init__(self, name):
        self.name = name
        ok
        super().__init__(500, 50, 80, 10, name)