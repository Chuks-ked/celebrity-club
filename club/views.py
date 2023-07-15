from django.shortcuts import render
from django.views.generic import CreateView
from .form import ContactForm
from .models import *
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    celeb = Celebrity.objects.all()
    return render(request, 'club/index.html',{
        'celeb': celeb,
    })

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
    celebs = Celebrity.objects.all()
    return render(request, 'club/celeb_list.html',{
        'celebs': celebs,
    })


def celeb_details(request, slug):
    celeb_detail = Celebrity.objects.get(slug = slug)
    return render(request, 'ris/property-details.html', {
        'celeb_detail':celeb_detail,
        })
