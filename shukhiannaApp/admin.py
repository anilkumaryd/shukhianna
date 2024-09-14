from django.contrib import admin

# Register your models here.
from .models import MainCategory,SubCategory,Product

admin.site.register((MainCategory,SubCategory,Product))
