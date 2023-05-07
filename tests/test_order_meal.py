import pytest
from lib.order_meal import *
from unittest.mock import Mock

"""
Initially #view_order returns an empty list
when no dishes have been added yet
"""
def test_view_order_initially_returns_empty_list():
    order_meal = OrderMeal()
    assert order_meal.view_order() == []

"""
Given a list of three mock dishes
with no mock dishes being selected
#selected_dishes returns an empty list
"""
def test_returns_empty_list_given_3_mock_dishes_with_none_selected():
    order_meal = OrderMeal()

    dish_1 = Mock()
    dish_1.selected = False

    dish_2 = Mock()
    dish_2.selected = False

    dish_3 = Mock()
    dish_3.selected = False

    dishes = Mock()
    dishes.all.return_value = [dish_1, dish_2, dish_3]

    order_meal.add_dishes(dishes)
    assert order_meal.view_order() == []

"""
Given a list of three mock dishes
with one dish being selected
#selected_dishes returns a list with one dish
"""
def test_returns_list_with_1_dish_given_3_mock_dishes_with_1_selected():
    order_meal = OrderMeal()

    dish_1 = Mock()
    dish_1.selected = False

    dish_2 = Mock()
    dish_2.selected = False

    dish_3 = Mock()
    dish_3.selected = True

    dishes = Mock()
    dishes.all.return_value = [dish_1, dish_2, dish_3]

    order_meal.add_dishes(dishes)
    assert order_meal.view_order() == [dish_3]

"""
Given a list of four mock dishes
with two dishes being selected
#selected_dishes returns a list with two dishes
"""
def test_returns_list_with_2_dishes_given_4_mock_dishes_with_2_selected():
    order_meal = OrderMeal()

    dish_8 = Mock()
    dish_8.selected = False

    dish_2 = Mock()
    dish_2.selected = True

    dish_7 = Mock()
    dish_7.selected = True

    dish_4 = Mock()
    dish_4.selected = False

    dishes = Mock()
    dishes.all.return_value = [dish_8, dish_2, dish_7, dish_4]

    order_meal.add_dishes(dishes)
    assert order_meal.view_order() == [dish_2, dish_7]

"""
Given a list of four mock dishes
with three dishes being selected
#total_price returns the total price
"""
def test_returns_total_price_given_4_mock_dishes_with_3_selected():
    order_meal = OrderMeal()

    dish_8 = Mock()
    dish_8.selected = True
    dish_8.price = 4.50

    dish_5 = Mock()
    dish_5.selected = True
    dish_5.price = 3.25

    dish_7 = Mock()
    dish_7.selected = False
    dish_7.price = 5.00

    dish_9 = Mock()
    dish_9.selected = True
    dish_9.price = 2.10

    dishes = Mock()
    dishes.all.return_value = [dish_8, dish_5, dish_7, dish_9]

    order_meal.add_dishes(dishes)
    assert order_meal.total_price() == 9.85

"""
Given a list of three dishes
with no dishes being selected
#place_order raises an error
"""
def test_raises_error_given_3_mock_dishes_with_none_selected():
    order_meal = OrderMeal()

    dish_2 = Mock()
    dish_2.selected = False

    dish_7 = Mock()
    dish_7.selected = False

    dish_4 = Mock()
    dish_4.selected = False

    dishes = Mock()
    dishes.all.return_value = [dish_2, dish_7, dish_4]

    order_meal.add_dishes(dishes)
    with pytest.raises(Exception) as err:
        order_meal.place_order(phone_num_to)
    error_message = str(err.value)
    assert error_message == "You have not selected a dish."

"""
Given a list of three dishes
with two dishes being selected
#place_order sends a text message 
to the verified mobile number
"""
def test_sends_text_message_given_3_mock_dishes_with_2_selected():
    order_meal = OrderMeal()

    dish_8 = Mock()
    dish_8.selected = True

    dish_3 = Mock()
    dish_3.selected = True

    dish_5 = Mock()
    dish_5.selected = False

    dishes = Mock()
    dishes.all.return_value = [dish_8, dish_3, dish_5]

    order_meal.add_dishes(dishes)
    assert order_meal.place_order(phone_num_to) == "Your message has been sent." 

"""
Given a list of three dishes
with two dishes being selected
and an unverified mobile number
#place_order raises an error
"""
def test_raises_error_given_unverified_number_3_mock_dishes_with_2_selected():
    order_meal = OrderMeal()

    dish_2 = Mock()
    dish_2.selected = False

    dish_7 = Mock()
    dish_7.selected = True

    dish_4 = Mock()
    dish_4.selected = True

    dishes = Mock()
    dishes.all.return_value = [dish_2, dish_7, dish_4]

    order_meal.add_dishes(dishes)
    with pytest.raises(Exception) as err:
        order_meal.place_order("+4445248590")
    error_message = str(err.value)
    assert error_message == "This number is unverified."