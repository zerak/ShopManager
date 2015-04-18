from django.contrib import admin
from .models import Shop, Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'area_id', 'add_date')
    list_filter = ('area_id',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Shop,ShopAdmin)