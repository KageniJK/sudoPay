import africastalking
from decouple import config, Csv

# Initialize SDK
# use 'sandbox' for development in the test environment
# username = config('AF_USERNAME')
# api_key = config('AF_KEY')
username = 'sudopay'
api_key = '5081377c43098290fd6dce414bf24af5ee2e0654bf0052ac8b6e4fb9ab77e8d5'

africastalking.initialize('sudopay',api_key)

payment = africastalking.Payment

def mpesa_checkout():
    try:
        # Initiate the checkout. If successful, you will get back a transactionId
        # transactionId = africastalking.PaymentService.mobile_checkout(productName,phoneNumber,currencyCode,amount,metadata)
        res = payment.mobile_checkout(
            product_name='testProduct', phone_number='+254729309658', currency_code='KES', amount=100.50, metadata={
                "agentId": "",
                "productId": "3366"
            })
        

        print ("The transactionId is " + res)

    except africastalking.Service.AfricasTalkingException as e:
        print("Received error response: %s" % str(e))


if __name__ == '__main__':

    # Specify the name of your Africa's Talking payment product
    productName = "testProduct"
    phoneNumber =  '0729309658'
    currencyCode = "KES"
    amount = 10.50
    metadata = {
        "agentId": "654",
        "productId": "3366"
        }

    # mpesa_checkout(productName,phoneNumber,currencyCode,amount,metadata)
    mpesa_checkout()
