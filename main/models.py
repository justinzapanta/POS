from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=250)
    product_code = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_img = models.ImageField(upload_to='./main/static/product-img', default=None)
    product_category = models.CharField(max_length=250)

    def __str__(self):
        return self.product_name
    

class Sales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    sales_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    sales_date = models.CharField(max_length=250)