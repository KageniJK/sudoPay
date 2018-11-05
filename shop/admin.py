from django.contrib import admin
from .models import Goodie , Category

# Register your models here.
admin.site.register (Goodie)
# admin.site.register(Quantity)
admin.site.register(Category)
