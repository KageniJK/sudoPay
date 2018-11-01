from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Goodie,Catalog

def index(request):
    try:
        products = Goodie.objects.all()
    except ObjectDoesNotExist as e :
        print(e)

    context = {
        'products' : products
    }
    return render(request,'shop/index.html' ,context )





