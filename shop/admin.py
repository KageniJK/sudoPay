from django.contrib import admin
from .models import Goodie , Catalog

# Register your models here.
admin.site.register (Catalog)
admin.site.register(Goodie)