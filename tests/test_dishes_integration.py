from lib.dishes import Dishes
from lib.dish import Dish

"""
Given three dishes
#all returns a list with three dishes
"""
def test_returns_list_with_3_dishes_given_3_dishes():
    dishes = Dishes()
    dish_1 = Dish("Chicken adobo", 4.50)
    dish_2 = Dish("Spring rolls", 2.00)
    dish_3 = Dish("Pancit bihon", 3.75)
    dishes.add(dish_1)
    dishes.add(dish_2)
    dishes.add(dish_3)
    assert dishes.all() == [dish_1, dish_2, dish_3]
