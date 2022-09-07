from django.contrib import admin
from .models import *
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name','last_name','email']

class ProductsAdmin(admin.ModelAdmin):
    fields = ['id', 'name','image','seller','price']

admin.site.register(users,UsersAdmin)
admin.site.register(Products,Products)