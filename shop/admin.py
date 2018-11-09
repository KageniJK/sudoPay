from django.contrib import admin
from .models import Goodie , Cart, Category,Profile

# Register your models here.
admin.site.register(Goodie)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Profile)
