# Generated by Django 4.2.5 on 2024-05-14 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_products_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_total_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_item_total_price',
            field=models.FloatField(),
        ),
    ]
