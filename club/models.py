from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.fullname
 