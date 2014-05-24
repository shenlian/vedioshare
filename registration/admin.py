# -*- coding: UTF-8 -*-

from django.contrib import admin
from registration.models import RegistrationProfile

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'activation_key_expired')
    search_fileds = ('user__username', 'user__first_name')
    
admin.site.register(RegistrationProfile, RegistrationAdmin)
