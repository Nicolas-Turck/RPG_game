from .character import Person

class Zombie(Person):

    def __init__(self, name=True):
        self.name = "Trump"
        super().__init__(600, 15, 14, 5, name) 