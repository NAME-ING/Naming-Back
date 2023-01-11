from django.contrib import admin
from dictionary.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'loginId', 'password']
    list_display_links = ['id', 'loginId']
