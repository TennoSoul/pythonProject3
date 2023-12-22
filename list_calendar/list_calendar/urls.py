from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('', include('events.urls')),
    path('admin/', admin.site.urls),
]