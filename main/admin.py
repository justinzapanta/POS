from django.contrib import admin
from .models import products, sales
# Register your models here.
admin.site.register([
    products,
    sales,
])