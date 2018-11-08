from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import CartForm,SignUpForm
from .camigo.camigo import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from multiprocessing import Process
from django.http import HttpResponse, Http404
from .models import Goodie,Category, Quantity, Cart
from django.views.generic import TemplateView


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
            setUpFace(username)
            trainSystem()
            user.save()
            login(request,user)
            return redirect('/')
    return render(request,'registration/registration.html',{"form":form})




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
        goodie = Goodie.objects.get(id=id)
        buyer = armSystem()
        print(buyer)
        # buyer='x'
        if buyer:
            user = User.objects.get(username=buyer)
            Cartform = CartForm(request.POST)
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
    armSystem()
    return redirect('index')



def search(request):

    if request.GET['goodie']:
        search_term = request.GET.get("goodie")
        goodie = sudopay.search_goodie(search_term)
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



  


    

    








