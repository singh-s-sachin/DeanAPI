from django.contrib import admin
from .models import authenticate
# Register your models here.
class authenticateAdmin(admin.ModelAdmin):
    list_display = ('name','email','uid','dob','regno','created','department')
admin.site.register(authenticate, authenticateAdmin)