from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Sign)
admin.site.register(contact_me)