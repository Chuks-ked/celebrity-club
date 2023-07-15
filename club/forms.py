from django import forms
from django.forms import ModelForm
from .models import Contact
from django.contrib import messages


# class ContactForm(ModelForm):
#     fullname = forms.CharField(max_length=100, widget = forms.TextInput(attrs={
#         'class' : 'form-control border-0 px-4 mb-3', 'placeholder': '','style':'height: 55px',
#     }))

#     email = forms.EmailField(label='Email', max_length=100, widget = forms.TextInput(attrs={
#         'class' : 'form-control border-0 px-4 mb-3', 'placeholder': '','style':'height: 55px',
#     }))

#     phone_number = forms.CharField(max_length=20, widget = forms.TextInput(attrs={
#         'class' : 'form-control border-0 px-4', 'placeholder': '','style':'height: 55px',
#     }))

#     message = forms.CharField(max_length=250, label='Message', widget=forms.Textarea(attrs={
#         'class' : 'form-control border-0 px-4', 'placeholder': '','style':'height: 55px',
#     }))

    
#     class Meta:
#         model = Contact
#         fields = '__all__'


class MeetForm(forms.Form):
    name     = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name', 'placeholder': 'Name', 'class': 'form-control'}))
    email    = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'id': 'email', 'placeholder': 'Email', 'class': 'form-control'}))
    phone_number    = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': 'phone_number', 'placeholder': 'Phone number', 'class': 'form-control'}))
    country  = forms.CharField(widget=forms.TextInput(attrs={'id': 'country',  'placeholder': 'Country', 'class': 'form-control'}))
    celebrity  = forms.CharField(widget=forms.TextInput(attrs={'id': 'celebrity',  'placeholder': 'Celebrity', 'class': 'form-control'}))
    message  = forms.CharField(widget=forms.Textarea(attrs={'id': 'message',  'placeholder': 'Message', 'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']

        if  '@' not in email:

            print("incorect email format")
            messages.error(self.request, 'incorrect email format')
            raise forms.ValidationError('incorrect email format')
        
        return email
    
