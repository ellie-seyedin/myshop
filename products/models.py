from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=70)
    logo =models.ImageField()
      
    def __str__(self):
      return f"{self.title}"
    
class Shirt(models.Model):
    title = models.CharField(max_length=70)
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)
    is_best_seller = models.BooleanField(default=False)
    
class Product(models.Model): 
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to="upload-img")
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name="prd")
    slug = models.SlugField(blank=True)
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
      return f"{self.title}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)