from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'weight')
    fields = ('name','price', 'weight')
