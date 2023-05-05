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