from django.shortcuts import render , redirect
from .generate_qr import generate_code

# from .APIs.message_receipt import *
# import APIs.message_receipt.send_receipt
import receipt

def generate_id ( request ):
    '''
    Customer wishes to have an ID of his/her own ! 
    '''
    customer = request.user.profile

    user_info = {
        'name' : customer.username ,
        'image': customer.profile_picture ,
        'mobile': request.user.phone_number ,
        'country': customer.country ,
        'email' : customer.email
    }

    generate_code(user_info)

    return redirect('profile')



def authenticate(request):
    '''
    User will now submit their auth ID so they can checkout
    '''
    
    return redirect('shop')



def check_out(request):
    '''
    once the checkout button has been pressed !
    '''

    test_message = "your order is as follows: bla bla"
    test_number = '254729309658'

    receipt.send_receipt(test_message,test_number)
    
    return redirect('shop')


