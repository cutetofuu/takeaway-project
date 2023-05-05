from lib.order_meal import OrderMeal
from lib.dishes import Dishes
from lib.dish import Dish

"""
Given a list of three dishes
with no dishes being selected
#selected_dishes returns an empty list
"""
def test_returns_empty_list_given_3_dishes_with_none_selected():
    order_meal = OrderMeal()
    dishes = Dishes()
    dish_1 = Dish("Chicken adobo", 4.50)
    dish_2 = Dish("Spring rolls", 2.00)
    dish_3 = Dish("Pancit bihon", 3.75)
    dishes.add(dish_1)
    dishes.add(dish_2)
    dishes.add(dish_3)
    order_meal.add_dishes(dishes)
    assert order_meal.view_order() == []

"""
Given a list of three dishes
with one dish being selected
#selected_dishes returns a list with one dish
"""
def test_returns_list_with_1_dish_given_3_dishes_with_1_selected():
    order_meal = OrderMeal()
    dishes = Dishes()
    dish_1 = Dish("Steak and chips", 5.50)
    dish_2 = Dish("Spring rolls", 2.00)
    dish_3 = Dish("Chicken tikka", 4.25)
    dishes.add(dish_1)
    dishes.add(dish_2)
    dishes.add(dish_3)
    dish_2.select_dish()
    order_meal.add_dishes(dishes)
    assert order_meal.view_order() == [dish_2]

"""
Given a list of four dishes
with two dishes being selected
#selected_dishes returns a list with two dishes
"""
def test_returns_list_with_2_dishes_given_4_dishes_with_2_selected():
    order_meal = OrderMeal()
    dishes = Dishes()
    dish_6 = Dish("Steak and chips", 5.50)
    dish_4 = Dish("Spring rolls", 2.00)
    dish_9 = Dish("Hunter's chicken", 3.75)
    dish_2 = Dish("Chicken tikka", 4.25)
    dishes.add(dish_6)
    dishes.add(dish_4)
    dishes.add(dish_9)
    dishes.add(dish_2)
    dish_9.select_dish()
    dish_2.select_dish()
    order_meal.add_dishes(dishes)
    assert order_meal.view_order() == [dish_9, dish_2]

"""
Given a list of four dishes
with three dishes being selected
#total_price returns the total price
"""
def test_returns_total_price_given_4_dishes_with_3_selected():
    order_meal = OrderMeal()
    dishes = Dishes()
    dish_6 = Dish("Steak and chips", 5.50)
    dish_4 = Dish("Spring rolls", 2.00)
    dish_9 = Dish("Hunter's chicken", 3.75)
    dish_2 = Dish("Chicken tikka", 4.25)
    dishes.add(dish_6)
    dishes.add(dish_4)
    dishes.add(dish_9)
    dishes.add(dish_2)
    dish_6.select_dish()
    dish_9.select_dish()
    dish_2.select_dish()
    order_meal.add_dishes(dishes)
    assert order_meal.total_price() == 13.50