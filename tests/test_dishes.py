from lib.dishes import Dishes

"""
Initially #all returns an empty list
when no dishes have been added yet
"""
def test_initially_returns_empty_list():
    dishes = Dishes()
    assert dishes.all() == []