from django.contrib import admin
from ecomapp.models import Product

# Register your models here.
# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','pname','price','is_active','pdetail','cat']
    list_filter=['cat','is_active','price']


admin.site.register(Product,ProductAdmin)    

