from django.shortcuts import render , redirect
from .generate_qr import generate_code
# from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

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



def check_out(request):
    '''
    once the checkout button has been pressed !
    '''
    
    return redirect('shop')
