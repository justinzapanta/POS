# Generated by Django 4.2.5 on 2024-05-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_img',
            field=models.ImageField(default=None, upload_to='./main/static/product-img'),
        ),
    ]
