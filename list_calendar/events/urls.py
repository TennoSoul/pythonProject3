# events\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events, name="list_events"),
    path('add_event', views.add_event, name="add-event"),
]
