from django.views.generic import FormView
from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


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



class VacationView(View):
    def get(self, request, *args, **kwargs):
        form = VacationForm()
        return render(request, 'club/vacation.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = VacationForm(request.POST)
        if form.is_valid():
            # Create a new vacation object and save the form data into the model
            vacation = Vacation(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                age=form.cleaned_data['age'],
                country=form.cleaned_data['country'],
                city=form.cleaned_data['city'],
                celebrity=form.cleaned_data['celebrity'],
                purpose=form.cleaned_data['purpose']
                # Add other fields from the form if applicable
            )
            vacation.save()
            # messages.success(self.request, "Profile details updated.")
            return redirect('home')  # Redirect to a thank-you page or any other page you desire after succes
        
        return render(request, 'club/vacation.html', {'form': form})


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'club/contact.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact object and save the form data into the model
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
                # Add other fields from the form if applicable
            )
            contact.save()
            # messages.success(self.request, "Profile details updated.")
            return redirect('home')  # Redirect to a thank-you page or any other page you desire after succes
        
        return render(request, 'club/contact.html', {'form': form})

def celeb_list(request):
    celebs = Celebrity.objects.all()
    return render(request, 'club/celeb_list.html',{
        'celebs': celebs,
    })


def celeb_details(request, slug):
    celeb_detail = Celebrity.objects.get(slug = slug)
    return render(request, 'club/celeb_details.html', {
        'celeb_detail':celeb_detail,
        })

class MeetView(View):
    def get(self, request, *args, **kwargs):
        form = MeetForm()
        return render(request, 'club/meet_greet.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = MeetForm(request.POST)
        if form.is_valid():
            # Create a new meetup object and save the form data into the model
            meetup = MeetUp(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                country=form.cleaned_data['country'],
                celebrity=form.cleaned_data['celebrity'],
                message=form.cleaned_data['message']
                # Add other fields from the form if applicable
            )
            meetup.save()
            # messages.success(self.request, "Profile details updated.")
            return redirect('home')  # Redirect to a thank-you page or any other page you desire after succes
        
        return render(request, 'club/meet_greet.html', {'form': form})

# class MeetView(FormView):
#     template_name = 'club/meet_greet.html'
#     form_class = MeetForm
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         self.send_mail(form.cleaned_data)
#         messages.success(self.request, 'Your response was submited successfuly.')
#         return super().form_valid(form)

#     def send_mail(self, valid_data):
#         name    = self.request.POST['name']
#         subject = self.request.POST['celebrity']
#         phone_number = self.request.POST['phone_number']
#         country = self.request.POST['country']
#         origin = self.request.build_absolute_uri().split('/')[:3]
#         origin = "/".join(origin)
#         html_message = render_to_string('core/email/contact-response.html', {'name':name, 'origin': origin})
#         plain_message = strip_tags(html_message)
#         email = self.request.POST['email']
#         message = self.request.POST['message']

#         from_email    = settings.EMAIL_HOST_USER
#         to_emails     = settings.WEBSITE_ADMIN_EMAILS

#         send_mail('ExtendGrowths', plain_message, from_email, [email], html_message=html_message, fail_silently=True)
#         send_mail(f'ExtendGrowths- admin(from: {email} - subject: {subject})', message, from_email, to_emails, fail_silently=True)
   