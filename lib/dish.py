class Dish:
    def __init__(self, name, price):
        if name == "" or price <= 0:
            raise Exception("Please add the correct details.")
        self.name = name
        self.price = price
        self.selected = False

    def select_dish(self):
        self.selected = True

    def format(self):
        return f'{self.name}, £{"%.2f" % self.price}'
