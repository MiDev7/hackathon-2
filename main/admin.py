from django.contrib import admin
from .models import *
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    fields = ['user', 'first_name','last_name']

class ProductsAdmin(admin.ModelAdmin):
    fields = [ 'name','image','seller','price']

admin.site.register(Customers,UsersAdmin)
admin.site.register(Products,ProductsAdmin)

admin.site.register(ShippingDetails)
admin.site.register(OrderItem)
admin.site.register(Order)