import africastalking as af
from decouple import config, Csv

# Initialize SDK

# use 'sandbox' for development in the test environment
username = config('AF_USERNAME')

# use your sandbox app API key for development in the test environment
api_key = config('AF_KEY')

af.initialize(username, api_key)



# card checkout
def make_payment():
    payment = af.Payment
    card = {
        'number': '3234324235452345',
        'countryCode': 'NG',
        'cvvNumber': 3343,
        'expiryMonth': 3,  # 1-12
        'expiryYear': 2022,  # > 2018
        'authToken': '3322'  # card pin
    }
    res = payment.card_checkout(product_name='TestProduct', currency_code='NGN',
                                amount=7822, payment_card=card, narration='Small Chops Checkout')
    print(res)

