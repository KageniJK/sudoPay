from django.shortcuts import render,redirect,get_object_or_404
from .generate_qr import generate_code
from qr_code.qrcode.utils import QRCodeOptions
from . import receipt , checkout
from decouple import config, Csv
from shop import models as md

import africastalking

def check_out(request ,product_id):
    '''
    once the checkout button has been pressed !
    '''
    customer = get_object_or_404(Profile,user=request.user)
    product = get_object_or_404( md.Goodie , pk=product_id )

    data = {
        'pn' : 'testProduct', 
        'phn': '+254'+str(customer.phone_number),
        'cc' : 'KES', 
        'am' : product.price, 
        'md' : {
            "ad": "654",
            "pd": "MK1144K"
        }
    }

    ck = checkout.mpesa_checkout(data)
    print(ck)
    
    message = "Dear "+customer.user.username.upper()+", your package "+product.name+" packageID: "+str(data['md']['pd'])+" KES:"+str(data['am'])+" ,has been processed ! Kindly , authorize cashout ."
    customer_number = '+254'+str(customer.phone_number)

    receipt.send_receipt(message,customer_number)
    
    context={
        'checkout' : ck ,
        'receipt' : message ,
        'product' : product ,
        'amount': data['cc']
    }
    
    return render( request , 'pay/confirmation.html' ,context )





def pay_index(request):
    return render(request,'pay/pay_index.html')

