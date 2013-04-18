from django.shortcuts import render
from django.http import Http404
from products.models import *

def index(request):
	return render(request, 'index.html')

def all_products(request):
    items = Item.objects.all()
    return render(request, 'all_products.html', {'items':items})

def all_category(request):
    categories = Category.objects.all()
    return render(request, 'all_category.html', {'categories':categories})

def category_browse(request, slug):
    categories = Category.objects.all()
    category = categories.get(slug=slug)
    items = Item.objects.all()
    items = items.filter(category=category)
    return render(request, 'category_browse.html', {'category':category, 'items':items})


def product_detail(request, slug):
    products = Item.objects.all()
    product = products.get(slug=slug)
    skus = SKU.objects.all()
    skus = skus.filter(item=product)
    return render(request, 'product_detail.html', {'product':product, 'skus':skus})
