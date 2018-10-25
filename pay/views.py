from django.shortcuts import render , redirect , get_object_or_404
from .generate_qr import generate_code
from qr_code.qrcode.utils import QRCodeOptions

from . import receipt
from .forms import *



def check_out(request):
    '''
    once the checkout button has been pressed !
    '''
    

    message = "your order is as follows: bla bla"
    customer_number = '254729309658'

    receipt.send_receipt(message,customer_number)

    
    return redirect('shop')


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
        'NAME': customer.user.username,
        'AVATAR': customer.profile_picture,
        'MOBILE': customer.phone_number,
        'CARD_NO' :bank_number ,
        'EXPIRY_DATE':expiry,
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
        acc_form = AccountForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and acc_form.is_valid():
            user_info = user_form.save(commit=False)
            profile_info = profile_form.save(commit=False)
            acc_info = acc_form.save(commit=False)
            user_info.save()
            profile_info.save()
            acc_info.owner = request.user
            acc_info.save()
            message = f"{request.user.username}'s account updated successfully !"

            return redirect('userprofile', request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        acc_form = AccountForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'acc_form' : acc_form ,
        'message': message
    }
    return render(request, 'profile/edit_profile.html', context)
