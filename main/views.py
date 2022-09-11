from contextlib import redirect_stderr
from sqlite3 import complete_statement
from unicodedata import name
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import JsonResponse
import json 


# Create your views here.
def main(request):
    return render(request, 'index.html',{})


def shop(request):
    return render(request, 'shop.html', {'products': Products.objects.all()})


def signup(request):
    if request.method == 'POST':
        form = user(request.POST)
        if form.is_valid():
            # get the value of the fields
           # create internal user 
            users = User.objects.create_user(
                user=request.POST['username'], 
                email=request.POST['email'], 
                password=request.POST['password'])
            Customers(
                username=users,
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            ).save()
            return redirect('/')
    else:    
        return render(request, 'signup.html',{'form':user()})

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else: 
        items = []
        order = {'get_cart_total':0,'get_cart_item':0}
    context = {'items' : items,'order' : order}


    return render(request, 'cart.html',context)

def updateCart(request):
   
    return JsonResponse('Item was added',safe=False)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else: 
        items = []
        order = {'get_cart_total':0,'get_cart_item':0}
    context = {'items' : items,'order' : order}

    return render(request,'checkout.html',context)