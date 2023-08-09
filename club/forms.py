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
    # celebrity = forms.CharField(max_length=100)
    celebrity = forms.ModelChoiceField(queryset=Celebrity.objects.all(), empty_label="Select a celebrity")
    purpose = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Vacation
        fields = '__all__'

class FancardAppForm(forms.ModelForm):
    fan_card = forms.ModelChoiceField(queryset=Fancard.objects.all(), empty_label="Select a card")
    # fan_card = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=256)
    age = forms.IntegerField()
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    # celebrity = forms.CharField(max_length=100)
    celebrity = forms.ModelChoiceField(queryset=Celebrity.objects.all(), empty_label="Select a celebrity")


    class Meta:
        model = FancardApp
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(FancardAppForm, self).__init__(*args, **kwargs)
    #     fan_card_choices = Fancard.objects.values_list('name', 'name').distinct()
    #     self.fields['fan_card'].widget = forms.Select(choices=fan_card_choices)

class MeetForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=256)
    country = forms.CharField(max_length=100)
    # celebrity = forms.CharField(max_length=100)
    celebrity = forms.ModelChoiceField(queryset=Celebrity.objects.all(), empty_label="Select a celebrity")
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = MeetUp
        fields = '__all__'

