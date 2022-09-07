from platform import mac_ver
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    class Meta:
        verbose_name_plural = "users"
    username = models.OneToOneField(User, null=True,on_delete=models.CASCADE,blank=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length = 150, null=True)
    email = models.EmailField(verbose_name='email', default='example@gmail.com', unique=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Products(models.Model):
    class Meta:
        verbose_name_plural = "Products"
    name = models.CharField(max_length=100, blank=False, null=True)
    image = models.ImageField(upload_to='Products/')
    seller = models.ForeignKey(users,on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places= 2)

    def __str__(self):
        return self.name

# class Order(models.Model):
#     user = models.ForeignKey(users, on_delete=models.SET_NULL,null=True,blank=True)


