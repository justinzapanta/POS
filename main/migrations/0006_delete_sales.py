# Generated by Django 4.2.5 on 2024-05-10 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_products_product_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sales',
        ),
    ]