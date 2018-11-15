from django.contrib import admin
from .models import Goodie , Catalog, Cart, Category

# Register your models here.
admin.site.register (Catalog)
admin.site.register(Goodie)
admin.site.register(Cart)
admin.site.register(Category)