class Dish:
    def __init__(self, name, price):
        if name == "" or price <= 0:
            raise Exception("Please add the correct details.")
        self.name = name
        self.price = price
        self.selected = False

    def select_dish(name):
        # Parameters:
        #   name: string representing the name of the dish
        # Side-effects:
        #   changes the selected property's value to True
        # Returns:
        #   none
        pass # No code here yet

    def format(self):
        # Parameters:
        #   none
        # Side-effects:
        #   none
        # Returns:
        #   a string displaying the name and price of a dish
        pass # No code here yet
