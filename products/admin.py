from django.contrib import admin
from .models import Product, Category, In_stock, Colour

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
    )
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class In_stockAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class ColourAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'colour_group',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(In_stock, In_stockAdmin)
admin.site.register(Colour, ColourAdmin)