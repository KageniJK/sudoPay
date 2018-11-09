from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import CartForm,SignUpForm
from .camigo.camigo import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from multiprocessing import Process
from django.http import HttpResponse, Http404
from .models import Goodie,Category, Cart,Profile
from django.views.generic import TemplateView
import time

def signup(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user=authenticate(username=username,email=email,password=password)
            profile=Profile(user=user)
            print('rada')
            profile.save()
            setUpFace(username)
            trainSystem()
            user.save()
            login(request,user)
            return redirect('/')
    return render(request,'registration/registration.html',{"form":form})


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





def index(request):
    Cartform = CartForm()
    try:
        products = Goodie.objects.all()
    except ObjectDoesNotExist as e :
        print(e)

    context = {
        'products' : products,
        'Cartform' : Cartform
    }
    return render(request,'shop/index.html' ,context )


def cart(request):
    items = Cart.objects.filter(paid='False')
    prices = []
    for item in items:
        if item.user == request.user:
            price = item.item.price
            prices.append(price)
            print(prices)
    total = sum(prices)
    return render(request,'cart.html',{"items":items,"total":total})
    
def add_to_cart(request,id):
    if request.method == 'POST':
        Cartform = CartForm(request.POST)
        goodie = Goodie.objects.get(id=id)
        if Cartform.is_valid():
            form = Cartform.save(commit=False)
            form.user = request.user
            form.item = goodie
            form.save()
            return redirect ('cart')
        print('error')
    print('x')

def delete_cart(request,id):
    item = Cart.objects.get(id=id)
    Cart.delete_item(item)
    return redirect('cart')

def empty(request):
    item =  Cart.objects.filter(user=request.user).delete()
    return redirect('cart')

def image(request):
    print('error')
    # setUpFace(request.user.username)
    # trainSystem(setUpFace(request.user.username))
    x = armSystem()
    print(x)
    return redirect('index')


def search(request):

    if request.GET['goodie']:
        search_term = request.GET.get("goodie")
        goodie = Goodie.search_goodie(search_term)
        message = f"{search_term}"

        return render(request,'search.html',locals())

    else:
        message = "You Haven't searched for any goodies"
        return render(request,'search.html',locals())





def stock(request,category_id):
    products = Goodie.objects.filter(category_id=category_id)
    stock = len(products)    

    if stock <=5:
        return HttpResponse('You are running out of stock for this category please re-stock')
    else:
        pass

# def current_stock(request,category_id):
#     if request.user.is_authenticated:
#         if  Goodie.objects.filter(category_id=category_id)
#             products = Goodie.objects.get(pk=category_id)
#             print(products)

#         return Goodies.objects.


# def current_stock(request,category_name):
#     if request.user.is_authenticated:
#     products = Category.objects.get(name=category_name)
#     goodie = category.picture.id
#     goodie = Picture.objects.filter(category_id=category_id)
#     # category.quantity = Category.quantity +=



# def kitchen_items(request,category_id):
#     goods = Goodie.objects.filter(category_id=category_id)
#     stock = len(goods)    

#     if stock <=5:
#         return HttpResponse('You are running out of stock for this category please re-stock')
#     else:
#         pass




# def groccery(request,category_id):
#     goods = Goodie.objects.filter(category_id=category_id)
#     stock = len(goods)    

#     if stock <=5:
#         return HttpResponse('You are running out of stock for this category please re-stock')
#     else:
#         pass




# def stationary(request,category_id):
#     goods = Goodie.objects.filter(category_id=category_id)
#     stock = len(goods)    

#     if stock <=5:
#         return HttpResponse('You are running out of stock for this category please re-stock')
#     else:
#         pass




# def hardware(request,category_id):
#     goods = Goodie.objects.filter(category_id=category_id)
#     stock = len(goods)    

#     if stock <=5:
#         return HttpResponse('You are running out of stock for this category please re-stock')
#     else:
#         pass

def waiter():
    while True:
        # print('rada')
        armSystem()
        # print('rada')
        continue

Process(target=waiter).start()

