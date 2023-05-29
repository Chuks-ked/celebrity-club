from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    fullname = forms.CharField(max_length=100, widget = forms.TextInput(attrs={
        'class' : 'form-control border-0 px-4 mb-3', 'placeholder': '','style':'height: 55px',
    }))

    email = forms.EmailField(label='Email', max_length=100, widget = forms.TextInput(attrs={
        'class' : 'form-control border-0 px-4 mb-3', 'placeholder': '','style':'height: 55px',
    }))

    phone_number = forms.CharField(max_length=20, widget = forms.TextInput(attrs={
        'class' : 'form-control border-0 px-4', 'placeholder': '','style':'height: 55px',
    }))

    message = forms.CharField(max_length=250, label='Message', widget=forms.Textarea(attrs={
        'class' : 'form-control border-0 px-4', 'placeholder': '','style':'height: 55px',
    }))

    
    class Meta:
        model = Contact
        fields = '__all__'
