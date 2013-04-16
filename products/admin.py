from django.contrib import admin
from products.models import Category, Item, SKU, Attribute, AttributeDetail

class CategoryAdmin(admin.ModelAdmin):
	fields = ['name', 'slug', 'parent', 'photo']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class SKUInline(admin.TabularInline):
	model = SKU

class ItemAdmin(admin.ModelAdmin):
	fields = ['category', 'name', 'slug', 'manufacturer', 'description', 'photo']
	list_display = ('name', 'category')
	prepopulated_fields = {'slug': ('name',)}
	inlines = [SKUInline]
admin.site.register(Item, ItemAdmin)

class AttributeDetailInline(admin.TabularInline):
	model = AttributeDetail
	
class SKUAdmin(admin.ModelAdmin):
	fields = ['item', 'sku_number', 'description', 'retail_price', 'unit_cost', 'quantity']
	list_display = ('sku_number', 'item', 'description')
	inlines = [AttributeDetailInline]
admin.site.register(SKU, SKUAdmin)

class AttributeInline(admin.TabularInline):
	model = Attribute

class AttributeDetailAdmin(admin.ModelAdmin):
	fields = ['sku', 'attribute', 'photo', 'value']
	list_display = ('sku', '__unicode__')
admin.site.register(AttributeDetail, AttributeDetailAdmin)

admin.site.register(Attribute)
