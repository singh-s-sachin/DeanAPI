from django.contrib import admin
from .models import post,follow,upcoming_feeds
admin.site.site_header = 'Sathyabama | Dean-dashboard'
admin.site.site_title = 'Sathyabama | Dean-app'
class postAdmin(admin.ModelAdmin):
    list_display = ('id','pid','description','attachment','time','date')
class followAdmin(admin.ModelAdmin):
    list_display = ('to','by','date')
class upcoming_feedsAdmin(admin.ModelAdmin):
    list_display = ('uid','seen')
admin.site.register(post,postAdmin)
admin.site.register(follow,followAdmin)
admin.site.register(upcoming_feeds,upcoming_feedsAdmin)