from django.db import models

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
