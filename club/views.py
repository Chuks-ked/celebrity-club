from django.shortcuts import render
from django.views.generic import CreateView
from .form import ContactForm
from .models import *
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

def celeb_list(request):
    celebs = Celebrity.objects.all()

    # search_input = request.GET.get('search-area')
    # if search_input:
    #     celebs = Celebrity.objects.filter(building_name__icontains=search_input)
    # else:
    #     celebs = Celebrity.objects.all()
    #     search_input = ''

    return render(request, 'club/celeb_list.html',{
        'celebs': celebs,
        # 'search_input':search_input
    })



