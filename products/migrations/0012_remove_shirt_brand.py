# Generated by Django 4.2.4 on 2023-08-15 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirt',
            name='brand',
        ),
    ]