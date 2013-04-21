from django.db import models
from shop.models import Product

class Category(models.Model):
	name = models.CharField(max_length=64)
	slug = models.SlugField(max_length=64)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
	photo = models.ImageField(upload_to='category_photos')
	
	def __unicode__(self):
		if self.parent:
			return u'%s -> %s' % (self.parent.name, self.name)
		return u'%s' % (self.name)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

class Item(Product):
	category = models.ForeignKey('Category', related_name='items')
	manufacturer = models.CharField(max_length=128)
	description = models.TextField()
	photo = models.ImageField(upload_to='item_photos', blank=True)

	def __unicode__(self):
		return u'%s: %s' % (self.category, self.name)
		
	class Meta:
		ordering = ['name']
