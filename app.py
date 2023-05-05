from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_num_from = os.getenv("TWILIO_NUMBER_FROM")
phone_num_to = os.getenv("TWILIO_NUMBER_TO")