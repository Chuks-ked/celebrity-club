from django.shortcuts import render
from django.views.generic import CreateView
from .form import ContactForm
from .models import Contact
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'club/index.html')

def fan_card(request):
    return render(request, 'club/fancard.html')

def fancard_app(request):
    return render(request, 'club/fancard_app.html')

def meet_greet(request):
    return render(request, 'club/meet_greet.html')

def vacation(request):
    return render(request, 'club/vacation.html')

def contact(request):
    return render(request, 'club/contact.html')

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'club/contact.html'
    success_url = reverse_lazy('home')


def celeb_list(request):
    return render(request, 'club/celeb_list.html')

