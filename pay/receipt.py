import africastalking as af
from decouple import config, Csv



def send_receipt(message, customer):
    # Initialize SDK
    username = config('AF_USERNAME')
    api_key = config('AF_KEY')

    af.initialize(username, api_key)

    # Initialize a service e.g. SMS
    receipt = af.SMS
    # Use the service synchronously

    customers = [
        "+"+customer,
        
        ]

    response = receipt.send(message, customers)
    print(response)

    # Or use it asynchronously

    def on_finish(error, response):
        if error is not None:
            raise error
        # print(response)
        return response

    # sms.send(message, ["+"+customer], callback=on_finish)

