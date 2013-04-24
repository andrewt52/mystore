from django.shortcuts import render_to_response, render, get_object_or_404
from products.models import Category
from django.template import RequestContext
from django.http import HttpResponse

def show_categories(request):
    return render_to_response("categories.html",
                          {'nodes':Category.objects.all()},
                          context_instance=RequestContext(request))

def category_detail(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return HttpResponse("%s" % category.name)

def categories(request):
	categories = Category.objects.filter(parent__isnull=True)
	return render(request, "categories.html", {'categories': categories})
