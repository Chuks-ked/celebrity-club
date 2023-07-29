from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=256)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = '__all__'


class VacationForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=256)
    age = forms.IntegerField()
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    celebrity = forms.CharField(max_length=100)
    purpose = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Vacation
        fields = '__all__'

class FancardAppForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=256)
    age = forms.IntegerField()
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    celebrity = forms.CharField(max_length=100)

    class Meta:
        model = FancardApp
        fields = '__all__'

class MeetForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=256)
    country = forms.CharField(max_length=100)
    celebrity = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = MeetUp
        fields = '__all__'




# class MeetForm(forms.Form):
#     name     = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name', 'placeholder': 'Name', 'class': 'form-control'}))
#     email    = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'id': 'email', 'placeholder': 'Email', 'class': 'form-control'}))
#     phone_number    = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': 'phone_number', 'placeholder': 'Phone number', 'class': 'form-control'}))
#     country  = forms.CharField(widget=forms.TextInput(attrs={'id': 'country',  'placeholder': 'Country', 'class': 'form-control'}))
#     celebrity  = forms.CharField(widget=forms.TextInput(attrs={'id': 'celebrity',  'placeholder': 'Celebrity', 'class': 'form-control'}))
#     message  = forms.CharField(widget=forms.Textarea(attrs={'id': 'message',  'placeholder': 'Message', 'class': 'form-control'}))

#     def clean_email(self):
#         email = self.cleaned_data['email']

#         if  '@' not in email:

#             print("incorect email format")
#             messages.error(self.request, 'incorrect email format')
#             raise forms.ValidationError('incorrect email format')
        
#         return email
    
