from django.contrib import admin
from .models import Product, Category, In_stock, Colour, Style, Material, Backing, Manufacturer, Comment

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

class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class BackingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name'
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
admin.site.register(Style, StyleAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Backing, BackingAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Comment, CommentAdmin)