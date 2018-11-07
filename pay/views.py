from django.shortcuts import render , redirect , get_object_or_404
from .generate_qr import generate_code
from qr_code.qrcode.utils import QRCodeOptions
from . import receipt , checkout
from .forms import *
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


def profile(request, user_username=None):

    '''
    Function view to a customer profile 
    '''

    profile = get_object_or_404(Profile, user__username=user_username)

    try:
        bank_info = get_object_or_404(Account, owner__username=user_username)
        bank_number = bank_info.card_number
        expiry = bank_info.expiry_date
    except:
        bank_info = None
        bank_number = 0000000000
        expiry = '2/2/2020'


    customer = request.user.profile

    user_info = {
        'name': customer.user.username,
        'image': customer.profile_picture,
        'MOBILE': customer.phone_number,
        'CARD_NO' :bank_number ,
        'expiry_date':expiry,
        'country': customer.country,
        'email': customer.user.email
    }

    data = {
        'profile': profile,
        'user_info': user_info
    }
    return render(request, 'profile/profile.html', data)



def update_profile(request):
    message = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST , request.FILES ,instance=request.user.profile)
        try:
            acc_form = AccountForm(request.POST,instance=request.user.account)
        except:
            acc_form = AccountForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and acc_form.is_valid():
            user_info = user_form.save(commit=False)
            profile_info = profile_form.save(commit=False)
            acc_info = acc_form.save(commit=False)
            user_info.save()
            profile_info.save()
            acc_info.owner = request.user
            acc_info.save()
            message = f"{request.user.username}'s: account updated successfully !"

            return redirect('userprofile', request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        try:
            acc_form = AccountForm(instance=request.user.account)
        except:
            acc_form = AccountForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'acc_form' : acc_form ,
        'message': message
    }
    return render(request, 'profile/edit_profile.html', context)


