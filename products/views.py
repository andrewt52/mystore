from django.shortcuts import render_to_response, render, get_object_or_404
from products.models import Category, Item
from django.template import RequestContext
from django.http import HttpResponse

def categories(request):
	categories = Category.objects.filter(parent__isnull=True)
	return render(request, "categories.html", {'categories': categories})

def category_detail(request, slug):
	category = get_object_or_404(Category, slug=slug)
	children = Category.objects.filter(parent=category)
	items = Item.objects.filter(category=category)
	return render(request, 'category_detail.html', {'category':category, 'children':children, 'items':items})

def search(request):
    if 's' in request.GET and request.GET['s']:
        s = request.GET['s']
        items = Item.objects.filter(name__icontains=s)
        return render(request, 'search_results.html',
            {'items': items, 'query': s})
    else:
        return render(request, 'search_failure.html')
