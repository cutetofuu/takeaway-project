class Dishes:
    def __init__(self):
        self._dishes = []

    def add(self, dish):
        self._dishes.append(dish)

    def all(self):
        return self._dishes
    