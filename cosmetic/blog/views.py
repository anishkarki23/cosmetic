from .models import Item
from django.shortcuts import render

from blog.models import Item

# Create your views here.

def home(request):

    q =  request.GET.get('q') if request.GET.get('q') != None else''

    items = Item.objects.all()

    context = {'items' : items }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
    
def contact(request):
    return render(request, 'blog/contact.html')

def shop(request):
    context = {}
    return render (request, 'blog/shop.html', context)

def cart(request):
    context = {}
    return render (request, 'blog/cart.html', context )

def checkout(request):
    context ={}
    return render (request, 'blog/checkout.html', context)
    