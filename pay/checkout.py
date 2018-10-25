import africastalking
from decouple import config, Csv

# Initialize SDK
username = config('AF_USERNAME')
api_key = config('AF_KEY')

sandname = config('SAND_USERNAME')
sandkey = config('SAND_KEY')

africastalking.initialize(sandname, sandkey)
# africastalking.initialize(username, api_key)

payment = africastalking.Payment


def mpesa_checkout():
    try:
        res = payment.mobile_checkout(
            product_name='testProduct', phone_number='+254729309658', currency_code='KES', amount=10, metadata={
                "agentId": "654",
                "productId": "3366"
            })

        print("The transactionId is " + str(res))

    except africastalking.Service.AfricasTalkingException as e:
        print("Received error response: %s" % str(e))
