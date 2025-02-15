from django.db import models
from django.urls import reverse


class Fancard(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    amount = models.IntegerField() 
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    recommend = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Vacation(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    celebrity = models.CharField(max_length=100)
    purpose = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class FancardApp(models.Model):
    fan_card = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    celebrity = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class MeetUp(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=250)
    country = models.CharField(max_length=100)
    celebrity = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

 
class Celebrity(models.Model):
    celebrity_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    about = models.TextField(max_length=1000)
   

    def __str__(self):
        return self.celebrity_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


