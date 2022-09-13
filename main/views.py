from contextlib import redirect_stderr
from math import prod
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import JsonResponse
import json 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def main(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total':0,'get_cart_item':0}
        cartItems = order['ger_cart_item']

    context = {'cartItems' : cartItems, 'customer': customer,}
    return render(request, 'index.html',context)


def shop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total':0,'get_cart_item':0}
        cartItems = order['ger_cart_item']

    context = {'products': Products.objects.all(),'cartItems' : cartItems}
    return render(request, 'shop.html', context)

def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total':0,'get_cart_item':0}
        cartItems = order['ger_cart_item']

    context = {'cartItems' : cartItems, 'customer': customer,}
    return render(request, 'home.html', context)

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            users1 = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + users1)
            return redirect('login')
            

    context = {'form': form}
    
    return render(request, 'signup.html',context)
    # if request.method == 'POST':
    #     form = user(request.POST)
    #     if form.is_valid():
    #         # get the value of the fields
    #        # create internal user 
    #         users = User.objects.create_user(
    #             user=request.POST['username'], 
    #             email=request.POST['email'], 
    #             password=request.POST['password'])
    #         Customers(
    #             username=users,
    #             first_name=request.POST['first_name'],
    #             last_name=request.POST['last_name']
    #         ).save()
    #         return redirect('/')
    # else:    
        

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total':0,'get_cart_item':0}
        cartItems = order['ger_cart_item']

    context = {'items' : items,'order' : order,'cartItems' : cartItems}


    return render(request, 'cart.html',context)

def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('ProcuctId: ', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId ) 

    order, created =  Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created =  OrderItem.objects.get_or_create(order=order, product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total':0,'get_cart_item':0}
        cartItems = order['ger_cart_item']

    context = {'items' : items,'order' : order, 'cartItems' : cartItems}

    return render(request,'checkout.html',context)


def processOrder(request):
    print('Data:', request.body)
    return JsonResponse('Payment complete!' , safe=False)

def loginPage(request):
    context = {}
    return  render(request, 'login.html', context)