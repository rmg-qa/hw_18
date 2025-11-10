import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv('MY_EMAIL')
name_sender = os.getenv('NAME_SENDER')
name_recipient = os.getenv('NAME_RECIPIENT')

URL = 'https://demowebshop.tricentis.com/'

request_body = {"giftcard_2.RecipientName": name_recipient,
                "giftcard_2.RecipientEmail": my_email,
                "giftcard_2.SenderName": name_sender,
                "giftcard_2.SenderEmail": my_email,
                "addtocart_2.EnteredQuantity": '1'
                }
