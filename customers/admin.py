from django.contrib import admin
from customers.models import Customer, CustomerAddress

class CustomerAddressInline(admin.TabularInline):
	model = CustomerAddress
	
class CustomerAdmin(admin.ModelAdmin):
	inlines = [CustomerAddressInline]
admin.site.register(Customer, CustomerAdmin)
