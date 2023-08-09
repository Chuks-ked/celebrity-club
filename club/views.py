from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from .models import *

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404



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


class FancardAppView(View):
    def get(self, request, slug, *args, **kwargs):
        fanapp = get_object_or_404(Fancard, slug=slug)
        form = FancardAppForm(instance=fanapp)
        return render(request, 'club/fancard_app.html', {'form': form, 'fanapp':fanapp})

    def post(self, request, slug, *args, **kwargs):
        fanapp = get_object_or_404(Fancard, slug=slug)
        form = FancardAppForm(request.POST, instance=fanapp)
        if form.is_valid():

            vacation = FancardApp(
                fan_card = form.cleaned_data['fan_card'],
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

        return render(request, 'club/fancard_app.html', {'form': form, 'fanapp':fanapp})


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

             # Send email to the user
            subject = 'Vacation Plan with celebrity'
            html_message = render_to_string('club/email/vacation_useremail.html', {'vacation': vacation})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, plain_message, from_email, [vacation.email], html_message=html_message, fail_silently=True)

            # Send email to the admin
            subject = 'New VACATION form submission'
            html_message = render_to_string('club/email/vacation_adminemail.html', {'vacation': vacation})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_emails = settings.WEBSITE_ADMIN_EMAILS
            send_mail(subject, plain_message, from_email, to_emails, html_message=html_message, fail_silently=True)

            return redirect('home')  # Redirect to a thank-you page or use a flash message
        
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
            subject = 'New CONTACT form submission'
            html_message = render_to_string('club/email/contact_adminemail.html', {'contact': contact})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_emails = settings.WEBSITE_ADMIN_EMAILS
            send_mail(subject, plain_message, from_email, to_emails, html_message=html_message, fail_silently=True)

            return redirect('home')  # Redirect to a thank-you page or use a flash message
        
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

            # Send email to the user
            subject = 'Meetup with celebrity'
            html_message = render_to_string('club/email/meet_useremail.html', {'meetup': meetup})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, plain_message, from_email, [meetup.email], html_message=html_message, fail_silently=True)

            # Send email to the admin
            subject = 'New MEETUP form submission'
            html_message = render_to_string('club/email/meet_adminemail.html', {'meetup': meetup})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_emails = settings.WEBSITE_ADMIN_EMAILS
            send_mail(subject, plain_message, from_email, to_emails, html_message=html_message, fail_silently=True)            
            # messages.success(self.request, "Profile details updated.")
            return redirect('home')  # Redirect to a thank-you page or any other page you desire after succes
        
        return render(request, 'club/meet_greet.html', {'form': form})
