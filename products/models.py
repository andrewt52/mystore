from django.db import models

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
		
class Item(models.Model):
	category = models.ForeignKey('Category', related_name='items')
	name = models.CharField(max_length=64)
	slug = models.SlugField(max_length=64)
	manufacturer = models.CharField(max_length=128)
	description = models.TextField()
	photo = models.ImageField(upload_to='item_photos', blank=True)

	def __unicode__(self):
		return u'%s: %s' % (self.category, self.name)
		
class SKU(models.Model):
	item = models.ForeignKey('Item', related_name='skus')
	description = models.CharField(max_length=64, verbose_name='Short Description')
	sku_number = models.IntegerField(verbose_name='SKU #')
	retail_price = models.DecimalField(max_digits=6, decimal_places=2)
	unit_cost = models.DecimalField(max_digits=6, decimal_places=2)
	quantity = models.IntegerField()
	
	def __unicode__(self):
		return u'%s - %d (%s)' % (self.item.name, self.sku_number, self.description)

	class Meta:
		verbose_name = 'SKU'
		verbose_name_plural = 'SKUs'
		
class Attribute(models.Model):
	name = models.CharField(max_length=64)
	description = models.TextField()
	
	def __unicode__(self):
		return self.name
		
class AttributeDetail(models.Model):
	sku = models.ForeignKey('SKU', related_name='sku_details', verbose_name='SKU')
	attribute = models.ForeignKey('Attribute', related_name='att_details')
	photo = models.ImageField(upload_to='attribute_images', blank=True)
	value = models.CharField(max_length=64)
	
	def __unicode__(self):
		return u'%s: %s' % (self.attribute.name, self.value)
		
	class Meta:
		verbose_name = 'Attribute Detail'
		verbose_name_plural = 'Attribute Details'
