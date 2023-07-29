from django.contrib import admin
from .models import *
# Register your models here.



class CelebrityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("celebrity_name",)}

class FancardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Contact)
admin.site.register(Vacation)
admin.site.register(FancardApp)
admin.site.register(MeetUp)

admin.site.register(Fancard, FancardAdmin)
admin.site.register(Celebrity, CelebrityAdmin)