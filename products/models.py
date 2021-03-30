from django.db import models
from django.contrib.auth.models import User

from profiles.models import User


class Category(models.Model):
    ''' 
    Categories model, connects with products model 
    to allow products to be grouped into categories
    '''

    class Meta: 
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


'''
The following models, 'in_stock', 'style', 'material', 'manufacturer', and 
'backing' are all carpet specifications, they're here as models
 to allow different specs to be displayed on product detail page.
They've all very similar, I set this up early on in the project 
and in future would set these all as fields in the same model
'''


class In_stock(models.Model):

    class Meta:
        verbose_name_plural = "In Stock"

    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Style(models.Model):

    class Meta:
        verbose_name_plural = "Styles"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Material(models.Model):

    class Meta:
        verbose_name_plural = "Material"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Backing(models.Model):

    class Meta:
        verbose_name_plural = "Backing"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Manufacturer(models.Model):

    class Meta:
        verbose_name_plural = "Manufacturer"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name



class Colour(models.Model):
    '''
    Model to allow user to select colour on product detail page. 
    Decided early on that this would have to be seperate to 
    product model because each colour needs to be linked to an image.
    '''
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=30, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True) 
    colour_group = models.CharField(max_length=254)
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    ''' 
    Products Model
    '''
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.ForeignKey('In_stock', null=True, blank=True, on_delete=models.SET_NULL)
    style = models.ForeignKey('Style', null=True, blank=True, on_delete=models.SET_NULL)
    material = models.ForeignKey('Material', null=True, blank=True, on_delete=models.SET_NULL)
    backing = models.ForeignKey('Backing', null=True, blank=True, on_delete=models.SET_NULL)
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey('Product', related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("date_added",)

    def __str__(self):
        return self.name