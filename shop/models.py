from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Category(models.Model):
    '''
    Items category
    '''
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.name


class Catalog(models.Model):
    '''
    Items category
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Goodie ( models.Model ):
    '''
    Basically this is Shop Items Model
    '''
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='static/shop',blank=True)
    category = models.ForeignKey(Catalog)
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
    

class Profile(models.Model):
    '''
    Profile of an customer . More Information .
    '''
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='static/profile', blank=True)
    phone_number = models.PositiveIntegerField( blank=True,null=True )
    country = CountryField(blank_label='(select country)' , null=True , blank=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_user_profile(cls, user):
        return cls.objects.get(user=user)

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

   