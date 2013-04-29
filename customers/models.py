from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
from django.contrib.auth.models import User
from django_localflavor_us.models import PhoneNumberField, USStateField

@receiver(post_save, sender=User)
def customer_creation_handler(sender, **kwargs):
	instance = kwargs['instance']
	Customer.objects.get_or_create(user=instance)

class Customer(models.Model):
	user = models.OneToOneField(User)
	# first name included in user model
	# last name included in user model
	# email included in user model
	phone_number = PhoneNumberField(blank=True)
	
	def __unicode__(self):
		return u'%s' % self.user.username

class CustomerForm(ModelForm):
        class Meta:
                model = Customer
                fields = ('phone_number', )

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
                fields = ('name','line_1','line_2','city','state','postalcode')
