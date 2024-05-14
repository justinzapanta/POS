from django.contrib import admin
from .models import Products, Invoice, Orders, Ingredients, Products_Ingredients
# Register your models here.
admin.site.register([
    Products, Invoice, Orders, Ingredients, Products_Ingredients
])