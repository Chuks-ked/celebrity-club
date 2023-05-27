from django.shortcuts import render

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

