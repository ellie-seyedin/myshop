# Generated by Django 4.2.4 on 2023-08-15 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_shirt_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand'),
        ),
    ]
