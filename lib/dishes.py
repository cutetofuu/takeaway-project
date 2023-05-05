class Dishes:
    def __init__(self):
        self._dishes = []

    def add(self, dish):
        self._dishes.append(dish)

    def all(self):
        view_dishes = list(map(lambda dish: f'{dish.name}, £{"%.2f" % dish.price}', self._dishes))
        return view_dishes