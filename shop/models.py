from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''
    Items category
    '''
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.name


class Goodie ( models.Model ):
    '''
    Basically this is Shop Items Model
    '''
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='static/shop',null=True, blank=True, default=0)
    category = models.ForeignKey(Category)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    catalog_date = models.DateField(auto_now=True)

    def add_goodie(self):
        '''
        Add an item to shelf
        '''
        return self.save()

    def delete_goodie(self):
        return self.delete()

    @classmethod
    def search_goodie(cls, search_term):
        goodie = cls.objects.filter(name__icontains=search_term)
        return goodie

    @classmethod
    def get_goodie_by_id(cls, id):
        goodie = cls.objects.get(pk=id)
        return goodie

    def current_stock(self):
        products = Goodie.objects.filter(goodie=self)
        total_products = 0
        for goods in goodie:
            total_goodie += goodie.quantity
        return self.goodie - total_goodie

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart')
    item = models.ForeignKey(Goodie,related_name='goodie')
    paid = models.CharField(default='False',max_length=20)

    def add_cart(self):
        return self.save()

    def delete_item(self):
        return self.delete()


    def __str__(self):
        return self.item.name

