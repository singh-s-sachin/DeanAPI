"""DeanAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('/', admin.site.urls),
    path('authenticate/', include('Auth.urls')),
    path('feeds/', include('posts.urls'))
]

















#403560850cce0c085a3e9e686c1d3b8ee20fa33cd501e2e55ddaa82b38feab57


#9897df78-fa37-11e9-8f0b-362b9e155667