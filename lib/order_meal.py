class OrderMeal:
    def __init__(self):
        self._selected_dishes = []

    def add_dishes(self, dishes):
        filtered_dishes = list(filter(lambda dish: dish.selected == True, dishes.all()))
        self._selected_dishes.extend(filtered_dishes)

    def view_order(self):
        return self._selected_dishes

    def total_price(self):
        return sum(list(map(lambda dish: dish.price, self._selected_dishes)))
    
    def place_order(self):
        # Parameters:
        #   none
        # Side-effects:
        #   none
        # Returns:
        #   a string text message confirming the order placement
        pass # No code here yet
