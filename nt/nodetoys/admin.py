from django.forms import TextInput
from nt.nodetoys.models import *
from django.contrib import admin
from django.db import models

class UserAdmin(admin.ModelAdmin):
    list_display = ("uid",)

admin.site.register(User,UserAdmin)

