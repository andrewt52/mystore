from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from mystore.forms import ContactForm

def profile(request):
	return HttpResponse("Account Profile")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thanks(request):
        return render(request, 'contact_thanks.html')
