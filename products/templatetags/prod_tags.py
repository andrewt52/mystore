from django import template
from products.models import Category

register = template.Library()

def category_tree():
	nodes = Category.objects.all()
	return {'nodes': nodes}

register.inclusion_tag('_categorytree.html')(category_tree)
