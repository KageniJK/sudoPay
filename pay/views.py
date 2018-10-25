from django.shortcuts import render , redirect , get_object_or_404
from .generate_qr import generate_code

import receipt
from .forms import *


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

    qr = generate_code(user_info)
    qr_info = Profile(instance = request.user.profile)
    qr_info.qr_id = qr
    qr_info.save()

    return redirect('profile',request.user.username)



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


def pay_index(request):
    return render(request,'pay_index.html')


def profile(request, user_username=None):
    '''
    Function view to a customer profile 
    '''
    profile = get_object_or_404(Profile, user__username=user_username)

    data = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html', data)



def update_profile(request):
    message = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST , request.FILES )
        acc_form = AccountForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and acc_form.is_valid():
            user_form.save()
            profile_form.save()
            acc_form.save()
            message = f"{request.user.username}'s account updated successfully !"

            return redirect('userprofile', request.user.username)
    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()
        acc_form = AccountForm()
    
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'acc_form' : acc_form ,
            'message': message
        }
        return render(request, 'profile/edit_profile.html', context)
