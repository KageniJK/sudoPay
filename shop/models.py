from django.db import models

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
    def get_goodie_by_id(cls,id):
        goodie = cls.objects.get(pk=id)
        return goodie

    
    def __str__(self):
        return self.name
