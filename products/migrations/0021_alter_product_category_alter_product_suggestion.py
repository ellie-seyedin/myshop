# Generated by Django 4.0 on 2023-09-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_product_category_alter_product_suggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='suggestion',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
