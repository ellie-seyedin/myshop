from django.db import models

# Create your models here.
class Address(models.Model):
   street = models.CharField(max_length=100)
   zipcode = models.CharField(max_length=10)
   city = models.CharField(max_length=20)
   country = models.CharField(max_length=20)
    
   def __str__(self):
      return f"{self.country} - {self.city}"

class Brand(models.Model):
    title = models.CharField(max_length=70)
    logo =  models.ImageField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null =True)
      
    def __str__(self):
      return f"{self.title}"
    
class Category(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)

    def __str__(self):
      return f"{self.title}"
    
class Product(models.Model): 
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category)
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