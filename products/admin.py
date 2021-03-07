from django.contrib import admin
from .models import Product, Category, In_stock, Colour

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(In_stock)
admin.site.register(Colour)