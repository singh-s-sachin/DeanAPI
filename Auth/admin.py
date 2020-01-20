from django.contrib import admin
from .models import authenticate
# Register your models here.
class authenticateAdmin(admin.ModelAdmin):
    list_display = ('name','email','uid','dob','regno','created','last_login','department')
admin.site.register(authenticate)