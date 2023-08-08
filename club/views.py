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
    plan = Fancard.objects.all()
    return render(request, 'club/fancard.html', {
        'plan' : plan
    })

# def fancard_app(request, slug):
#     fanapp = Fancard.objects.get(slug = slug)
#     return render(request, 'club/fancard_app.html',{
#         'fanapp': fanapp
#     })


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

def fancard_app(request, slug):
    fanapp = Fancard.objects.get(slug = slug)
    return render(request, 'club/fancard_app.html',{
        'fanapp': fanapp
    })

from django.shortcuts import render, get_object_or_404
from .models import Fancard

class FancardAppView(View):
    def get(self, request, slug, *args, **kwargs):
        fanapp = get_object_or_404(Fancard, slug=slug)
        form = FancardAppForm(instance=fanapp)
        return render(request, 'club/fancard_app.html', {'form': form})

    def post(self, request, slug, *args, **kwargs):
        fanapp = get_object_or_404(Fancard, slug=slug)
        form = FancardAppForm(request.POST, instance=fanapp)
        if form.is_valid():

            vacation = Fancard(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                age=form.cleaned_data['age'],
                country=form.cleaned_data['country'],
                city=form.cleaned_data['city'],
                celebrity=form.cleaned_data['celebrity'],
                
            )
            vacation.save()

            return redirect('home')

        return render(request, 'club/fancard_app.html', {'fanapp': fanapp})


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

            # Send email to the user
            subject = 'Thank you for contacting us celebrity'
            html_message = render_to_string('club/email/contact_useremail.html', {'contact': contact})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, plain_message, from_email, [contact.email], html_message=html_message, fail_silently=True)

            # Send email to the admin
            subject = 'New contact form submission'
            html_message = render_to_string('club/email/contact_adminemail.html', {'contact': contact})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_emails = settings.WEBSITE_ADMIN_EMAILS
            send_mail(subject, plain_message, from_email, to_emails, html_message=html_message, fail_silently=True)

            # admin_message = f'A new contact form has been submitted.\nName: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}'
            # admin_from_email = settings.EMAIL_HOST_USER  # Replace with your actual email address
            # admin_to_email = settings.WEBSITE_ADMIN_EMAILS  # Replace with the admin's email address
            # send_mail(subject, admin_message, admin_from_email, admin_to_email, fail_silently=True)

            # html_message = render_to_string('core/email/new-withdrawal-alert.html', {'name': name, 'amount': amount, 'btcn_addr': btcn_addr, 'nationality': nationality, 'date': date, 'origin': origin})
            # plain_message = strip_tags(html_message)
            # from_email = settings.EMAIL_HOST_USER
            # to_emails = settings.WEBSITE_ADMIN_EMAILS
            # send_mail('ExtendGrowths-New Withdrawal Alert!', plain_message, from_email, to_emails, html_message=html_message, fail_silently=True)


            return redirect('home')  # Redirect to a thank-you page or any other page you desire after succes
        
        return render(request, 'club/contact.html', {'form': form})


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
   