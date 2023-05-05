from lib.dishes import Dishes
from unittest.mock import Mock

"""
Initially #all returns an empty list
when no dishes have been added yet
"""
def test_all_initially_returns_empty_list():
    dishes = Dishes()
    assert dishes.all() == []

"""
Given three mock dishes
#all returns a list with three dishes
"""
def test_returns_list_with_3_dishes_given_3_mock_dishes():
    dishes = Dishes()

    dish_7 = Mock()
    dish_4 = Mock()
    dish_9 = Mock()

    dishes.add(dish_7)
    dishes.add(dish_4)
    dishes.add(dish_9)
    assert dishes.all() == [dish_7, dish_4, dish_9]
