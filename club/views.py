from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import FormView
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

def contact(request):
    return render(request, 'club/contact.html')

class ContactView(CreateView):
    model = Contact
    form_class = MeetForm
    template_name = 'club/contact.html'
    success_url = reverse_lazy('home')


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


class MeetView(FormView):
    template_name = 'club/meet_greet.html'
    form_class = MeetForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        messages.success(self.request, 'Your response was submited successfuly.')
        return super().form_valid(form)

    def send_mail(self, valid_data):
        name    = self.request.POST['name']
        subject = self.request.POST['celebrity']
        phone_number = self.request.POST['phone_number']
        country = self.request.POST['country']
        origin = self.request.build_absolute_uri().split('/')[:3]
        origin = "/".join(origin)
        html_message = render_to_string('core/email/contact-response.html', {'name':name, 'origin': origin})
        plain_message = strip_tags(html_message)
        email = self.request.POST['email']
        message = self.request.POST['message']

        from_email    = settings.EMAIL_HOST_USER
        to_emails     = settings.WEBSITE_ADMIN_EMAILS

        send_mail('ExtendGrowths', plain_message, from_email, [email], html_message=html_message, fail_silently=True)
        send_mail(f'ExtendGrowths- admin(from: {email} - subject: {subject})', message, from_email, to_emails, fail_silently=True)
   