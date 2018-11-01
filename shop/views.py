from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Goodie,Cart
from .forms import CartForm
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
       price = item.item.price
       prices.append(price)
    print(prices)
    total = sum(prices)
    return render(request,'cart.html',{"items":items,"total":total})

def add_to_cart(request,id):
    if request.method == 'POST':
        goodie = Goodie.objects.get(id=id)
        Cartform = CartForm(request.POST)
        if Cartform.is_valid():
            form = Cartform.save(commit=False)
            form.user = request.user
            form.item = goodie
            form.save()
            return redirect ('cart')
    print('x')

def delete_cart(request,id):
    item = Cart.objects.get(id=id)
    Cart.delete_item(item)
    return redirect('cart')

def empty(request):
    item =  Cart.objects.filter(user=request.user).delete()
    return redirect('cart')