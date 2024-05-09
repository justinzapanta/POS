from django.contrib import admin
from .models import Products, Sales
# Register your models here.
admin.site.register([
    Products,
    Sales,
])