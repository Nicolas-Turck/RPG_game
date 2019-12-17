from .character import Person

class Orc(Person):
    
    def __init__(self, name=True):
        self.name = "Lepen"
        super().__init__(400, 40, 70, 20, name)
    
