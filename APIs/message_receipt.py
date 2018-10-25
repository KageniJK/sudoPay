import africastalking as af 
from decouple import config, Csv

# Initialize SDK
username = config('AF_USERNAME')
api_key = config('AF_KEY')

af.initialize(username, api_key)





def send_receipt( message , customer):
    # Initialize a service e.g. SMS
    sms = af.SMS
    # Use the service synchronously
    response = sms.send(message, ["+"+customer])
    print(response)

    # Or use it asynchronously
    def on_finish(error, response):
        if error is not None:
            raise error
        print(response)

    sms.send(message, ["+"+customer], callback=on_finish)


if __name__ == '__main__':

    test_message = "your order is as follows: bla bla"
    test_number = '254728258626'
    
    send_receipt(test_message,test_number)
