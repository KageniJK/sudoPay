import africastalking
from decouple import config, Csv

def mpesa_checkout(data):
    username = config('AF_USERNAME')
    api_key = config('AF_KEY')

    sandname = config('SAND_USERNAME')
    sandkey = config('SAND_KEY')

    africastalking.initialize(sandname, sandkey)
    # africastalking.initialize(username, api_key)

    payment = africastalking.Payment
    try:
        res = payment.mobile_checkout(product_name=data['pn'],
                                       phone_number=data['phn'],
                                       currency_code=data['cc'],
                                       amount=data['am'],
                                       metadata={
                                           'agentId':data['md']['ad'],
                                           'productId':data['md']['pd']
                                       }                                        )

        print("The transactionId is " + str(res))
        return res

    except africastalking.Service.AfricasTalkingException as e:
        print("Received error response: %s" % str(e))
