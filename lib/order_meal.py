from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import sys
sys.path.append("..") 
from app import *
from datetime import datetime, timedelta

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
    
    def place_order(self, num_sent_to):
        if len(self._selected_dishes) == 0:
            raise Exception("You have not selected a dish.")
        else:
            current_datetime = datetime.now() + timedelta(minutes=40)
            delivery_time = current_datetime.strftime("%H:%M")

            client = Client(account_sid, auth_token)

            try:
                client.messages.create(
                    to=num_sent_to,
                    from_=phone_num_from,
                    body=f"Thank you! Your order was placed and will be delivered before {delivery_time}")
                return "Your message has been sent."
            except TwilioRestException:
                raise Exception("This number is unverified.")
