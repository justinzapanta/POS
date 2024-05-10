from django.contrib import admin
from .models import Products, Invoice, Orders
# Register your models here.
admin.site.register([
    Products, Invoice, Orders
])