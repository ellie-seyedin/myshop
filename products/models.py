from django.db import models

# Create your models here.

class Shirt(models.Model):
    title = models.CharField(max_length=70)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
      return f"{self.title}"