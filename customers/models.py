from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django_localflavor_us.models import PhoneNumberField, USStateField

class Customer(models.Model):
	user = models.OneToOneField(User)
	# first name included in user model
	# last name included in user model
	# email included in user model
	phone_number = PhoneNumberField(blank=True)

class CustomerForm(ModelForm):
        class Meta:
                model = Customer

        
class CustomerAddress(models.Model):
	customer = models.ForeignKey(Customer)
	name = models.CharField(max_length=150)
	line_1 = models.CharField(max_length=300)
	line_2 = models.CharField(max_length=300, blank=True)
	city = models.CharField(max_length=150)
	state = USStateField(blank=True)
	postalcode = models.CharField(max_length=10)

class CustomerAddressForm(ModelForm):
        class Meta:
                model = CustomerAddress
