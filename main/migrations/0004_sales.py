# Generated by Django 4.2.5 on 2024-05-09 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sales_id', models.AutoField(primary_key=True, serialize=False)),
                ('sales_date', models.CharField(max_length=250)),
                ('sales_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
        ),
    ]
