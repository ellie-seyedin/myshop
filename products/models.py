from django.db import models

# Create your models here.

class Shirt(models.Model):
    title = models.CharField(max_length=70)
    price = models.PositiveIntegerField()

# In your script or interactive shell with command: python3 manage.py shell  
from products.models import Shirt 
new_shirt = Shirt(1,"Long_sleeve shirt", 20) 
new_shirt.save()

# Or If I don't want to store in a variable
from products.models import Shirt 
Shirt(2,"Sport polo shirt", 35).save()