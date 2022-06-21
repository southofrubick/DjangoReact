from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price')
    fieldsets = [
        (None,                          {'fields': ['product_name']}),
        ('description',                          {'fields': ['product_description']}),
        ('Date information',      {'fields': ['product_price']}),
    ]

admin.site.register(Product, ProductAdmin)