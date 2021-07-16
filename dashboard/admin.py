from django.contrib import admin

from .models import Product, Sales

from django.contrib.auth.models import Group

#Customise the Admin Header
admin.site.site_header = 'SUCCESS POS Dashboard'

#Customize The Display of Model in a Table inside the Admin Pannel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'costprice', 'sellingprice', 'quantity')

# Register your models here and also pass your class Admin for List Display if available.
admin.site.register(Product,ProductAdmin)
admin.site.register(Sales)
#admin.site.unregister(Group)
