from django.contrib import admin
from dictionary.models import *


@admin.register(User)
class accountsAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'password']
    list_display_links = ['id', 'firstName']
