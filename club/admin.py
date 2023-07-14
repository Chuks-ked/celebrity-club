from django.contrib import admin
from .models import *
# Register your models here.



class CelebrityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("celebrity_name",)}

admin.site.register(Contact)
admin.site.register(Celebrity, CelebrityAdmin)