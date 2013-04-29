from django.shortcuts import render_to_response, render, get_object_or_404
from customers.models import *
from django.forms.models import modelform_factory, modelformset_factory
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class UserForm(ModelForm):
        class Meta:
                model = User
                fields = ('username', 'first_name', 'last_name', 'email',)

                
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/profile/form/address')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def address_form(request):
    
    if request.user.is_authenticated():
        if request.method == 'POST':
            customer = Customer.objects.get(user = request.user)
            customer_address = CustomerAddress(customer = customer)
            form = CustomerAddressForm(request.POST, instance = customer_address)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/profile/')
        else:
            form = CustomerAddressForm()
        return render(request, 'address_form.html', {'form': form})
    else:
        return HttpResponseRedirect('accounts/login/')

def profile(request):
    if request.user.is_authenticated():
        customer = Customer.objects.get(user = request.user)
        customer_addresses = CustomerAddress.objects.filter(customer=customer)
        return render(request, 'profile.html', {'customer':customer, 'addresses': customer_addresses})


    return HttpResponseRedirect('/accounts/login/')

def edit_profile(request):
    if request.user.is_authenticated():
        profile = request.user

        if request.method == 'POST':
            form = UserForm(request.POST, instance = profile)
            if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/accounts/profile/')
        else:
            form = UserForm(instance = profile)
        return render(request, 'edit_profile.html', {'form': form})

    return HttpResponseRedirect('/accounts/profile/')

def change_number(request):
    if request.user.is_authenticated():
        
        customer = Customer.objects.get(user = request.user)
        if request.method == 'POST':
            form = CustomerForm(request.POST, instance = customer)
            if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/accounts/profile/')
        else:
            form = CustomerForm(instance = customer)
        return render(request, 'customer_form.html', {'form': form})
    else:
        return HttpResponseRedirect('/accounts/login/')

def delete_address(request, address_number):
    
    if request.user.is_authenticated():
        
        customer = Customer.objects.get(user = request.user)
        customer_addresses = CustomerAddress.objects.filter(customer=customer)

        index = int('0' + address_number) - 1
        
        try:
            customer_address = customer_addresses[index]
        except:
            return HttpResponseRedirect('/accounts/profile/')
        
        
        
        customer_address.delete()
        return HttpResponseRedirect('/accounts/profile/')
    else:
        return HttpResponseRedirect('/accounts/login/')

def edit_address(request, address_number):
    
    if request.user.is_authenticated():
        
        customer = Customer.objects.get(user = request.user)
        customer_addresses = CustomerAddress.objects.filter(customer=customer)

        index = int('0' + address_number) - 1
        
        try:
            customer_address = customer_addresses[index]
        except:
            return HttpResponseRedirect('/accounts/profile/')
        
        
        if request.method == 'POST':
            form = CustomerAddressForm(request.POST, instance = customer_address)
            
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/profile/')
        else:
            form = CustomerAddressForm(instance = customer_address)
        return render(request, 'edit_address.html', {'form': form, 'number':address_number})
    else:
        return HttpResponseRedirect('/accounts/login/')
