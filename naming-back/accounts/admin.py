from django.contrib import admin
from dictionary.models import *

@admin.register(accounts)
class accountsAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName']
    list_display_links = ['id', 'firstName']