from django.contrib import admin

from models import Item, Category

admin.site.register(Item)

class CategoryAdmin(admin.ModelAdmin):
	fields = ['name', 'slug', 'parent', 'photo']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)
