from django.shortcuts import render_to_response, render, get_object_or_404
from customers.models import *
from django.forms.models import modelform_factory, modelformset_factory
from django.template import RequestContext
from django.http import HttpResponseRedirect

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/profile/form/address')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def add_address(request):
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = CustomerAddressForm()
    return render(request, 'address_form.html', {'form': form})
