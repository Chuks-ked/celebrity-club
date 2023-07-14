from django.db import models
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.fullname
 
class Celebrity(models.Model):
    celebrity_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    about = models.TextField(max_length=1000)
   

    def __str__(self):
        return self.celebrity_name
    
    # @property
    # def tenant_registration_url(self):
    #     return reverse('demo',kwargs={
    #         'slug':self.slug
    #     })

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
