"""Models for product app"""
from django.db import models


class Category(models.Model):
    """Category model"""

    class Meta:
        """
        Adjust the verbose name or the plural form of it from
        the Django defaults
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """Return the friendly name"""
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
