# Takeaway Multi-Class Planned Design Recipe

## 1. Describe the Problem

> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.
> 
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.
> 
> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total.

Use the `twilio-python` package to implement this next one. You will need to use
mocks too.

> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered.


Fair warning: if you push your Twilio API Key to a public GitHub repository,
anyone will be able to see and use it. What are the security implications of
that? How will you keep that information out of your repository?

## 2. Design the Class System

```
  ┌────────────────────────────┐
  │  OrderMeal                 │
  │                            │
  │  - selected_dishes(dishes) │
  │  - total_price()           │
  │  - place_order()           │
  │                            │
  └─────────────┬──────────────┘
                │
                │ owns a list of
                │
    ┌───────────▼───────────┐
    │  Dishes               │
    │                       │
    │  - add(dish)          │
    │  - all()              │
    │                       │
    └───────────┬───────────┘
                │ owns a list of
                │
     ┌──────────▼─────────┐
     │  Dish              │
     │                    │
     │  - name            │
     │  - price           │
     │  - selected        │
     │  - format()        │
     │                    │
     └────────────────────┘

```

_Also design the interface of each class in more detail._

```python

class OrderMeal:
    def selected_dishes(dishes):
        # Parameters:
        #   dishes: a list of all the Dish objects
        # Side-effects:
        #   none
        # Returns:
        #   a list of all the selected Dish objects
        pass # No code here yet

    def total_price(self):
        # Parameters:
        #   none
        # Side-effects:
        #   none
        # Returns:
        #   a float of the total price of all selected Dish objects
        pass # No code here yet

    def place_order():
        # Parameters:
        #   none
        # Side-effects:
        #   none
        # Returns:
        #   a string text message confirming the order placement
        pass # No code here yet


class Dishes:
    def __init__(self):
        # Side-effects:
        #   Sets the dishes properties
        pass # No code here yet

    def add(self, dish):
        # Parameters:
        #   dish: an instance of Dish
        # Side-effects:
        #   Adds the dish to the dishes property of the self object
        # Returns:
        #   none
        pass # No code here yet

    def all(self):
        # Parameters:
        #   none
        # Side-effects:
        #   none
        # Returns:
        #   a list of all the Dish objects
        pass # No code here yet

class Dish:
    # User-facing properties:
    #   name: string
    #   price: float with 2 decimal points
    #   selected: bool

    def __init__(self, name, price):
        # Side-effects:
        #   Sets the name, price and selected properties
        pass # No code here yet

    def selected(name):
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

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
Given two dishes
#all returns a list with two dishes
"""
dishes = Dishes()
dish_1 = Dish("Chicken adobo", 4.50)
dish_2 = Dish("Spring rolls", 2.70)
dishes.add(dish_1)
dishes.add(dish_2)
dishes.all() # => ["Chicken adobo, £4.50", "Spring rolls, £2.70"]

"""
Given two dishes
with one dish
#selected_dishes returns a list with two dishes
"""
dishes = Dishes()
dish_1 = Dish("Chicken adobo", 4.50)
dish_2 = Dish("Spring rolls", 2.70)
order_meal = OrderMeal()
dishes.add(dish_1)
dishes.add(dish_2)
dish_2.selected()
order_meal.selected_dishes(dishes) # => ["Spring rolls, £2.70"]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

"""
Given empty strings for the name and price
Raises an error
"""
with pytest.raises(Exception) as err:
    dish = Dish("", "")
error.message = str(err.value)
error.message # => "You haven't added a dish."

"""
Given a name and a price
Returns the dish's name
"""
dish = Dish("Chicken adobo", 4.50)
dish.name # => "Chicken adobo"

"""
Given a name and a price
Returns the dish's price
"""
dish = Dish("Chicken adobo", 4.50)
dish.price # => 4.50
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
