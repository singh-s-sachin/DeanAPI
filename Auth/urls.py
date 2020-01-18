from django.urls import path,include
from . import views
from rest_framework import routers

#router.register('accounts',views.accountview)
urlpatterns = [
	path('signin',views.create),
    path('create',views.update),
    path('test',views.test),
]
