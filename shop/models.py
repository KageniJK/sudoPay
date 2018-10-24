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
    category = models.ForeignKey(Catalog)
    description = models.TextField()
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