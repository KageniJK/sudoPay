from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Goodie,Category, Quantity
from django.views.generic import TemplateView
from django.contrib.auth.models import User


def index(request):
    try:
        products = Goodie.objects.all()
    except ObjectDoesNotExist as e :
        print(e)

    context = {
        'products' : products
    }
    return render(request,'shop/index.html' ,context )





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


def current_stock(request,category_name):
    if request.user.is_authenticated:
    products = Category.objects.get(name=category_name)
    goodie = picture.id
    goodie = Picture.objects.filter(category_id=category_id)
    category.quantity = Category.quantity +=







        





























































# def electronics(request,category_id):
#     goods = Goodie.objects.filter(category_id=category_id)
#     stock = len(goods)    

#     if stock <=5:
#         return HttpResponse('You are running out of stock for this category please re-stock')
#     else:
#         pass




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



  


    

    







