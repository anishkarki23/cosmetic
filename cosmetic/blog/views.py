from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
    
def contact(request):
    return render(request, 'blog/contact.html')

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render (request, 'blog/shop.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render (request, 'blog/cart.html', context )

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 , 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render (request, 'blog/checkout.html', context)
    