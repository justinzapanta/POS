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
    

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_item = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    order_item_total_price = models.IntegerField()
    order_date = models.CharField(max_length=250)


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_order_number = models.IntegerField()
    invoice_total_price = models.IntegerField()
    invoice_date = models.CharField(max_length=250)
