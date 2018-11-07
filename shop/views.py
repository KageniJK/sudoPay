from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Goodie,Cart
from .forms import CartForm,SignUpForm
from .camigo.camigo import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from multiprocessing import Process


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

    








# def waiter():

#     while True:
#         print('rada')
#         watcher = watcher(imageRoot, cascade)
#         watcher.watch()
#         # pass
#         print('rada')
#         continue

# Process(target=waiter).start()