import pytest
from lib.dish import Dish

"""
Given an empty string for the name
Raises an error
"""
def test_raises_error_given_empty_string_as_name():
    with pytest.raises(Exception) as err:
        dish = Dish("", 2.00)
    error_message = str(err.value)
    assert error_message == "Please add the correct details."

"""
Given a value of zero for the price
Raises an error
"""
def test_raises_error_given_zero_as_price():
    with pytest.raises(Exception) as err:
        dish = Dish("Cottage pie", 0.00)
    error_message = str(err.value)
    assert error_message == "Please add the correct details."

"""
Given a value of -2 for the price
Raises an error
"""
def test_raises_error_given_negative_2_as_price():
    with pytest.raises(Exception) as err:
        dish = Dish("Cottage pie", -2.00)
    error_message = str(err.value)
    assert error_message == "Please add the correct details."

"""
Given a name and a price
Returns the dish's name as a string
"""
def test_returns_name_given_name_and_price():
    dish = Dish("Chicken adobo", 4.50)
    assert dish.name == "Chicken adobo"
    assert type(dish.name) == str

"""
Given a name and a price
Returns the dish's price as a float
"""
def test_returns_price_given_name_and_price():
    dish = Dish("Chicken adobo", 4.50)
    assert dish.price == 4.50
    assert type(dish.price) == float

"""
Given a name and a price
Returns the dish's selected status as False
"""
def test_returns_selected_as_false_given_name_and_price():
    dish = Dish("English breakfast", 5.00)
    assert dish.selected == False

"""
Given a name and a price
#select_dish changes the dish's selected status to True
"""
def test_select_dish_returns_selected_as_true_given_name_and_price():
    dish = Dish("Toad in the hole", 3.50)
    dish.select_dish()
    assert dish.selected == True

"""
Given a name and a price
#format returns the name and price as a formatted string
"""
def test_format_returns_string_given_name_and_price():
    dish = Dish("Chicken tikka", 3.00)
    assert dish.format() == "Chicken tikka, £3.00"
