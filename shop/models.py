from django.db import models
from django.contrib.auth.models import User

class Catalog(models.Model):
    '''
    Items category
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    picture = models.ImageField(upload_to='shopping',blank=True)
    category = models.ForeignKey(Category,related_name='category')
    description = models.TextField()
    price = models.PositiveIntegerField()
    catalog_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def add_goodie(self):
        '''
        Add an item to shelf
        '''
        return self.save()

    def delete_goodie(self):
        return self.delete()

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