from django.db import models


class Product(models.Model):
    barcode = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_vegan = models.BooleanField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

