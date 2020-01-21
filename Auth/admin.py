from django.contrib import admin
from .models import authenticate
# Register your models here.
admin.site.site_header = 'Sathyabama | Dean-dashboard'
admin.site.site_title = 'Sathyabama | Dean-app'
class authenticateAdmin(admin.ModelAdmin):
    list_display = ('name','email','uid','regno','created','last_login')
admin.site.register(authenticate, authenticateAdmin)