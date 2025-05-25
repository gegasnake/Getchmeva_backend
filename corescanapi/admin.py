from django.contrib import admin
from .models import Product
# Register your models here.


# Register Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'name', 'is_vegan']
    search_fields = ['barcode', 'name']
